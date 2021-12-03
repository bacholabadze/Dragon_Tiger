import React, { useEffect, useState } from "react";
import axios from "axios";
import "./index.css";
const Home = () => {
  const [games, setGames] = useState([]);

  const getGames = async () => {
    const response = await axios.get("http://localhost:8000/api/get/all/game");
    setGames(response.data);
  };

  useEffect(() => {
    getGames();
  }, []);
  console.log(games);
  const renderGames = () => {
    return games.map((game) => {
      return (
        <section>
          <p>Table Name: {game.name}</p>
          <p>Min bet on this table: {game.minBet}</p>

          <a href={`http://localhost:3000/game/${game._id}`}>{game._id}</a>
        </section>
      );
    });
  };

  return (
    <div className="container">
      <div className="tb">{renderGames()}</div>
    </div>
  );
};

export default Home;
