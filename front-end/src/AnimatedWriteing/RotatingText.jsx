import React, { useEffect } from "react";
import "./temp.scss";

const RotatingText = () => {
  useEffect(() => {
    // Select words and prepare letters
    let words = document.querySelectorAll(".word");
    words.forEach((word) => {
      let letters = word.textContent.split("");
      word.textContent = "";
      letters.forEach((letter) => {
        let span = document.createElement("span");
        span.textContent = letter;
        span.className = "letter";
        word.append(span);
      });
    });

    let currentWordIndex = 0;
    let maxWordIndex = words.length - 1;
    words[currentWordIndex].style.opacity = "1";

    const rotateText = () => {
      let currentWord = words[currentWordIndex];
      let nextWord =
        currentWordIndex === maxWordIndex ? words[0] : words[currentWordIndex + 1];

      // Rotate out letters of current word
      Array.from(currentWord.children).forEach((letter, i) => {
        setTimeout(() => {
          letter.className = "letter out";
        }, i * 80);
      });

      // Reveal and rotate in letters of next word
      nextWord.style.opacity = "1";
      Array.from(nextWord.children).forEach((letter, i) => {
        letter.className = "letter behind";
        setTimeout(() => {
          letter.className = "letter in";
        }, 340 + i * 80);
      });

      currentWordIndex =
        currentWordIndex === maxWordIndex ? 0 : currentWordIndex + 1;
    };

    rotateText();
    const intervalId = setInterval(rotateText, 4000);

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  return (<>
    <div className="BOX">
      <div className="rotating-text">
        <p>Fii un cititor</p>
        <p>
          <span className="word alizarin">atent.</span>
          <span className="word wisteria">bine informat.</span>
          <span className="word peter-river">înțelept.</span>
          <span className="word emerald">critic.</span>
          <span className="word sun-flower">responsabil.</span>
        </p>
      </div>
    </div>
    </>
  );
};

export default RotatingText; 

