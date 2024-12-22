import React from "react";
import Header from "../Header/Header";
import Footer from "../Footer/Footer";

const newsArray = [
	{ title: "Breaking News 1", link: "https://example.com/news1" },
	{ title: "Breaking News 2", link: "https://example.com/news2" },
	{ title: "Breaking News 3", link: "https://example.com/news3" },
	{ title: "Breaking News 4", link: "https://example.com/news4" },
	{ title: "Breaking News 5", link: "https://example.com/news5" },
	{ title: "Breaking News 6", link: "https://example.com/news6" },
	{ title: "Breaking News 7", link: "https://example.com/news7" },
	{ title: "Breaking News 8", link: "https://example.com/news8" },
	{ title: "Breaking News 9", link: "https://example.com/news9" },
	{ title: "Breaking News 10", link: "https://example.com/news10" },
	{ title: "Breaking News 11", link: "https://example.com/news11" },
	{ title: "Breaking News 12", link: "https://example.com/news12" },
	{ title: "Breaking News 13", link: "https://example.com/news13" },
	{ title: "Breaking News 14", link: "https://example.com/news14" },
];

const Fake = () => {
	return (
		<>
        <Header></Header>
			<div className="news-page">
				<h1 className="news-title">Cele mai recente stiri fake</h1>
				<div className="news-container">
					{newsArray.map((news, index) => (
						<div className="news-item" key={index}>
							<a href={news.link} target="_blank" rel="noopener noreferrer" className="news-link">
								{news.title}
							</a>
						</div>
					))}
				</div>
			</div>
            <Footer></Footer>
		</>
	);
};

export default Fake;
