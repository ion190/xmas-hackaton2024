import React, { useState } from "react";
import "./HomePage.css"; // Asigură-te că ai un fișier CSS separat pentru stiluri
import Header from "../Header/Header";
import RotatingText from "../AnimatedWriteing/RotatingText";
import Footer from "../Footer/Footer";

const HomePage = () => {
	const [inputText, setInputText] = useState("");

	const handleChange = (e) => {
		setInputText(e.target.value);
	};

	const handleSubmit = () => {
		// Procesați textul introdus în continuare aici
		console.log(inputText);
	};

	return (
		<>
			<Header></Header>

			<div className="home-page">
				<div className="rectangle">
					<div className="TextWrapperFront">
						<RotatingText></RotatingText>
						<p className="Meassajul">Nu te lăsa influențat de zvonuri sau informații false! Folosește aplicația noastră pentru a fi mereu informat corect și în siguranță.</p>
					</div>
					<img src="/FrontImage.png" alt="Front Image" />
				</div>

				<div className="textarea-container">
					<p className="InputParagraf">Adevărul se află la un clic distanță</p>
					<div className="ForRelativePos">
						<textarea className="input-textarea" value={inputText} onChange={handleChange} placeholder="Introduceti un text pentru a fi procesat..." />
						{/* Butonul va apărea doar dacă există text în inputText */}
						{inputText.trim() !== "" && (
							<button className="submit-button" onClick={handleSubmit}>
								Verifcă  
							</button>
						)}
					</div>
				</div>
			</div>

			<Footer />
		</>
	);
};

export default HomePage;
