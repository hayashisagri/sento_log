import "leaflet/dist/leaflet.css";
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";

import { Visit } from "@/components/visit";
import { Sento } from "@/types/sento";
import axios from "axios";
import L from "leaflet";
import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";
import { useEffect, useState } from "react";

// @ts-ignore
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconUrl: markerIcon.src,
  iconRetinaUrl: markerIcon2x.src,
  shadowUrl: markerShadow.src,
});

const Map = (props) => {
  const [sentos, setSentos] = useState<Sento[]>([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/v1/sentos")
      .then((res) => {
        setSentos(res.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <MapContainer
      center={[35.813889715185397, 139.79037467390296]}
      zoom={12}
      scrollWheelZoom={true}
      style={{ height: "100vh", width: "100%", marginTop: "10px" }}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {sentos.map((sento: Sento, index) => (
        <Marker
          key={index}
          position={[
            JSON.parse(sento.point_geojson).coordinates[1],
            JSON.parse(sento.point_geojson).coordinates[0],
          ]}
        >
          <Popup>
            <h2>{sento.name}</h2>
            <dl>
              <Visit
                userId={props.userId}
                sentoId={sento.id}
                visitedSento={props.visitedSento}
              />
              <dt>紹介</dt>
              <dd>{sento.description}</dd>
              <dt>住所</dt>
              <dd>{sento.address}</dd>
              <dt>営業時間</dt>
              <dd>{sento.time_open}</dd>
              <dt>定休日</dt>
              <dd>{sento.day_close}</dd>
              <dt>アクセス</dt>
              <dd>{sento.station_distance}</dd>
              <dt>ホームページ</dt>
              <dd>{sento.homepage_url}</dd>
            </dl>
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default Map;
