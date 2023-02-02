import { Button } from "react-bootstrap";

export const Logout = (props) => {
  const onClickLogout = async () => {
    await localStorage.removeItem("access");
    await window.location.reload();
  };

  return (
    <div style={{marginBottom: '20px', textAlign: 'center'}}>
      <h2>こんにちは、{props.name}さん</h2>
      <Button block="true" size="lg" type="submit" onClick={onClickLogout}>
        Logout
      </Button>
    </div>
  );
};
