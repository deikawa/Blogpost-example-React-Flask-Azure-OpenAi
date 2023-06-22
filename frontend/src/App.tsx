import axios from "axios";
import { useState } from "react";
const apiUrl = "http://localhost:8080/";

export const postPrompt = async (prompt: string) => {
  try {
    const payload = {
      prompt: prompt,
    };

    const response = await axios.post(apiUrl, payload, {});
    return response.data;
  } catch (error) {
    console.log(error);
  }
};

function App() {
  const [response, setResponse] = useState("");

  const handleClick = async () => {
    const response = await postPrompt("Give me a good blogpost idea");
    setResponse(response.response);
  };

  return (
    <div>
      <h2>{response}</h2>
      <button onClick={handleClick}>Send prompt</button>
    </div>
  );
}

export default App;
