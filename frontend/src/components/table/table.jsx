import { useEffect, useRef, useState } from "react";
import "./index.css";
const Table = ({
  gameSpec,
  sendCard,
  card,
  handleChange,
  handleChangeBet,
  tigerCard,
  dragonCard,
  socket,
  start_timestamp,
}) => {
  console.log(start_timestamp);
  const [seconds, setSeconds] = useState(15);
  const [renderBet, setRenderBets] = useState(true);
  const [dragonOn, setDragonOn] = useState(true);
  const [tigerOn, setTigerOn] = useState(false);

  useEffect(() => {
    if (seconds !== undefined) {
      let myInterval = setInterval(() => {
        if (seconds > 0) {
          setSeconds(seconds - 1);
        }
        if (seconds === 0) {
          clearInterval(myInterval);
          setRenderBets(false);
        }
      }, 1000);
      return () => {
        clearInterval(myInterval);
      };
    }
  }, [seconds]);

  const handleClickOnBets = (e) => {
    const data = {
      amount: e.target.value,
      type: dragonOn ? "dragon" : "tiger",
      game_round_id: gameSpec.game_round_id,
    };
    socket.current.emit("place_bet", data);
  };

  const renderBets = () => {
    if (renderBet) {
      return (
        <>
          <div className="chips">
            <button value={1} onClick={handleClickOnBets}>
              1
            </button>
            <button value={5} onClick={handleClickOnBets}>
              5
            </button>
            <button value={10} onClick={handleClickOnBets}>
              10
            </button>
          </div>
        </>
      );
    }
  };
  const renderClickedButton = () => {
    if (dragonOn) {
      return (
        <div>
          <h1>Dragon</h1>
        </div>
      );
    } else {
      return (
        <div>
          <h1>Tiger</h1>
        </div>
      );
    }
  };

  return (
    <div className="cr">
      <div className="table">
        <h1>welcome to the table</h1>
        <p>min_bet: {gameSpec.min_bet || ""}</p>
        <p>max_bet: {gameSpec.max_bet || ""}</p>
        <form>
          <input
            placeholder="Deal card..."
            type="text"
            className="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChange}
            value={card}
          />
          <button onClick={sendCard}>Submit</button>
          <h3 className="time">{seconds}</h3>
        </form>
        <button
          onClick={(e) => {
            setDragonOn(true);
            setTigerOn(false);
          }}
        >
          Dragon
        </button>
        <button
          onClick={(e) => {
            setTigerOn(true);
            setDragonOn(false);
          }}
        >
          Tiger
        </button>
        {renderClickedButton()}
        {renderBets()}
        <div className="scaned">
          <p>Dragon Card: {dragonCard}</p>
          <p> </p>
          <p>Tiger Card: {tigerCard}</p>
        </div>
      </div>
    </div>
  );
};

export default Table;
