import {useEffect, useState} from "react";


export const App = () => {
  const [name, setName] = useState('')

  useEffect(() => {
    (
      async () => {
        const response = await fetch('http://localhost:8080/............', {
          headers: {'Content-Type': 'application/json'},
          credentials: 'include',
        })
        const content = await response.json()

        setName(content.name)
      }
    )()
  })

  return (
    <div className={App}>
      <Nav name={name} setName={setName()} />
      <main>

      </main>
    </div>

  )
}