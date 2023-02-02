import { User } from "@/types/user";
import axios from "axios";
import { useState } from "react";
import { Button, Form } from "react-bootstrap";

export const Signup = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [re_password, setRePassword] = useState("");
  const [message, setMessage] = useState("");

  const validateForm = () => {
    if (
      email.length > 0 &&
      password.length > 0 &&
      name.length > 0 &&
      re_password.length > 0
    ) {
      return password === re_password;
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setName("");
    setEmail("");
    setPassword("");
    setRePassword("");
  };

  const onClickSignup = async () => {
    await axios
      .post<User>("http://localhost:8000/api/auth/users/", {
        name: name,
        email: email,
        password: password,
        re_password: re_password,
      })
      .then((res) => {
        setMessage("emailを確認してください");
      })
      .catch((err) => {
        console.log(err.response.status);
        err.response.status === 400
          ? setMessage(err.response.data.email[0])
          : setMessage("errorが発生しました。再度お試しください");
      });
  };

  return (
    <>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="name">
          <Form.Label>名前</Form.Label>
          <Form.Control
            autoFocus
            type="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="email">
          <Form.Label>Email</Form.Label>
          <Form.Control
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="password">
          <Form.Label>パスワード</Form.Label>
          <Form.Control
            autoFocus
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="re_password">
          <Form.Label>パスワード（確認）</Form.Label>
          <Form.Control
            autoFocus
            type="password"
            value={re_password}
            onChange={(e) => setRePassword(e.target.value)}
          />
        </Form.Group>
        <Button
          size="lg"
          type="submit"
          disabled={!validateForm()}
          onClick={onClickSignup}
        >
          会員登録
        </Button>
      </Form>
      <div>{message}</div>
    </>
  );
};
