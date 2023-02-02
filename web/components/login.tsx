import { User } from "@/types/user";
import axios from "axios";
import { useState } from "react";
import { Button, Form } from "react-bootstrap";

export const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const validateForm = () => {
    return email.length > 0 && password.length > 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setEmail("");
    setPassword("");
  };

  const onClickLogin = async () => {
    await axios
      .post<User>("http://localhost:8000/api/auth/jwt/create/", {
        email: email,
        password: password,
      })
      .then((res) => {
        localStorage.setItem("access", res.data.access);
      })
      .then(() => {
        window.location.reload();
      })
      .catch((err) => {
        console.error(err);
      });
  };

  return (
    <>
      <div>ログインしてください</div>
      <Form onSubmit={handleSubmit}>
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
        <Button
          size="lg"
          type="submit"
          disabled={!validateForm()}
          onClick={onClickLogin}
        >
          Login
        </Button>
      </Form>
    </>
  );
};
