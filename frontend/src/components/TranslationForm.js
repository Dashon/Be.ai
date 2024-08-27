import React, { useState } from "react";
import axios from "axios";

const TranslationForm = () => {
  const [text, setText] = useState("");
  const [translatedText, setTranslatedText] = useState("");

  const handleTranslate = async () => {
    console.log("text");
    const response = await axios.post("http://localhost:8000/translate/", {
      text: text,
      source_lang: "en",
      target_lang: "aave",
    });
    console.log(response.data);
    setTranslatedText(response.data.translated_text);
  };

  return (
    <div>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text to translate"
      />
      <button onClick={handleTranslate}>Translate</button>
      {translatedText && (
        <div>
          <h3>Translated Text:</h3>
          <p>{translatedText}</p>
        </div>
      )}
    </div>
  );
};

export default TranslationForm;
