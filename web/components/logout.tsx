import { Button } from "react-bootstrap";

export const Logout = (props) => {
  const onClickLogout = async () => {
    await localStorage.removeItem("access");
    await window.location.reload();
  };

  return (
    <>
      <div>こんにちは、{props.name}さん</div>
      <Button block="true" size="lg" type="submit" onClick={onClickLogout}>
        Logout
      </Button>
    </>
  );
};
