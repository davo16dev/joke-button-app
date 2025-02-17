import React from "react";
import { Typewriter } from "react-simple-typewriter";
import useJokes from "../hooks/useJokes";
import "./Button.css";

const Button: React.FC = () => {
  const { jokes, loading, error, getJoke } = useJokes();

  return (
    <div className="container">
      <div
        className="button-wrapper"
        style={{
          position: "fixed",
          top: "15px",
          left: 0,
          width: "100%",
          textAlign: "center",
          zIndex: 1000,
        }}
      >
        <button className="joke-button" onClick={getJoke} disabled={loading}>
          {loading ? "Loading..." : "Get a Joke"}
        </button>
      </div>

      <div className="jokes-scroll-wrapper">
        <div className="jokes-scroll">
          {error && <p className="text-danger">{error}</p>}
          {[...jokes].map((joke, index) => (
            <div key={jokes.length - index} className="typing-container">
              <Typewriter
                words={[`- ${joke}`]}
                loop={1}
                cursor
                cursorStyle="|"
                typeSpeed={10}
                deleteSpeed={0}
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Button;
