import React from "react";
import "./Header.css"; // Importă fișierul CSS pentru stiluri
import { useNavigate, useLocation } from "react-router-dom"; // Import useNavigate și useLocation

const Header = () => {
  const location = useLocation(); // Obține locația curentă
  const navigate = useNavigate();

  // Funcția care schimbă ruta
  const handleButtonClick = (path) => {
    navigate(path); // Navighează către ruta specificată
  };

  return (
    <header className="header">
      <div className="logo">
        <img src="/ClarFact.png" alt="Logo" />
      </div>
      <div className="HeaderButtons">
        <button
          className={location.pathname === "/" ? "active" : "default"} // Verifică dacă ruta curentă este "/"
          onClick={() => handleButtonClick("/")}
        >
          Verifica
        </button>
        <button
          className={location.pathname === "/News" ? "active" : "default"} // Verifică dacă ruta curentă este "/News"
          onClick={() => handleButtonClick("/News")}
        >
          Citeste stiri
        </button>
        <button
          className={location.pathname === "/Fake" ? "active" : "default"} // Verifică dacă ruta curentă este "/"
          onClick={() => handleButtonClick("/Fake")}
        >
          Fakes
        </button>
      </div>
    </header>
  );
};

export default Header;
