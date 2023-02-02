import axios from "axios";
import { useEffect, useState } from "react";

export const Visit = (props) => {
  const user = props.userId;
  let sentoId = props.sentoId;
  const sentos = Object.entries(props.visitedSento);
  const [visit, setVisit] = useState(false);

  let visitedList = [];
  if (sentoId) {
    sentos.map((sento) => {
      visitedList.push(sento[1].sento.id);
    });
  }

  useEffect(() => {
    const checkVisited = () => {
      if (visitedList.includes(sentoId)) {
        setVisit(true);
      }
    };
    checkVisited();
  }, [sentoId]);

  const isAuthenticatedAndVisited = (useId) => {
    return useId !== 0;
  };

  const onClickPostVisit = () => {
    axios
      .post("http://localhost:8000/api/v1/sento/visits/", {
        user: props.userId,
        sento: props.sentoId,
      })
      .then((res) => {});
    setVisit(true);
  };

  const onClickDeleteVisit = () => {
    const body_params = {
      sento: props.sentoId,
      user: props.userId,
    };
    axios
      .delete("http://localhost:8000/api/v1/sento/visits/", {
        data: body_params,
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    setVisit(false);
  };

  return (
    <>
      {visit ? (
        <button onClick={onClickDeleteVisit}>訪問済み</button>
      ) : (
        <button
          disabled={!isAuthenticatedAndVisited(user)}
          onClick={onClickPostVisit}
        >
          未訪問
        </button>
      )}
    </>
  );
};
