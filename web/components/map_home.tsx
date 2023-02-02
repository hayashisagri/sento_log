import dynamic from "next/dynamic";
import React from "react";

export const MapPage = (props) => {
  const Map = React.useMemo(
    () =>
      dynamic(() => import("../components/map"), {
        loading: () => <p>A map is loading</p>,
        ssr: false,
      }),
    []
  );
  return <Map userId={props.userId} visitedSento={props.visitedSento} />;
};
