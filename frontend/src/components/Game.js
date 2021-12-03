import React, { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import io from "socket.io-client";
import Table from "./table/table";

const Game = () => {
  const { id } = useParams();
  const [gameSpec, setGameSpec] = useState({});
  const [card, setCard] = useState("");
  const [bet, setBet] = useState("");
  const [target, setTarget] = useState("");
  const [dragonCard, setDragonCard] = useState("")
  const [tigerCard, setTigerCard] = useState("")

  const socket = useRef(null);

  const handleChange = (e) => {
    setCard(e.target.value);
  };

  const handleChangeBet = (e) => {
    setBet(e.target.value);
  };

  const handleChangeTarget = (e) => {
    setTarget(e.target.value);
  };

  useEffect(() => {
    socket.current = io("http://localhost:8000", {
      path: "/ws/socket.io",
      query: { game_id: id },
      transports: ["websocket"],
    });
  }, []);

  useEffect(() => {
    socket.current.on("on_connect_data", (data) => {
      setGameSpec(data);
    });
  }, []);

  useEffect(() => {
    socket.current.on("send_dragon_card", (data) => {
      setDragonCard(data.card)
    })
  }, [])


  useEffect(() => {
    socket.current.on("send_tiger_card", (data) => {
      setTigerCard(data.card)
    })
  }, [])

  const sendCard = (e) => {
    e.preventDefault();
    socket.current.emit("scan_card", {
      card: card,
      game_round_id: gameSpec.game_round_id
    });
  };

  const sendBet = (e) => {
    e.preventDefault();
    socket.current.emit("receive_bet", {
      bet: bet,
    });
  };

  const sendTarget = (e) => {
    e.preventDefault();
    socket.current.emit("receive_target", {
      target: target,
    });
  };

  return (
    <div>
      <Table
        gameSpec={gameSpec}
        sendCard={sendCard}
        sendBet={sendBet}
        card={card}
        handleChange={handleChange}
        handleChangeBet={handleChangeBet}
        bet={bet}
        handleChangeTarget={handleChangeTarget}
        target={target}
        sendTarget={sendTarget}
        dragonCard={dragonCard}
        tigerCard={tigerCard}
        socket={socket}
        start_timestamp={gameSpec.start_timestamp}
      />
    </div>
  );
};

export default Game;
