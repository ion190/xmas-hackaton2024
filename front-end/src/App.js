import HomePage from "./HomePage/HomePage";
import NewsPage from "./NewsPage/News";
import Fake from "./FakePage/Fake";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"; // Import corect

function App() {
    return (
		<Router>
			<Routes>
                <Route path="/Fake" element={<Fake />}></Route>
                <Route path="/News" element={<NewsPage />}></Route>
				<Route path="/" element={<HomePage />}></Route>
			</Routes>
		</Router>
	);
}

export default App;
