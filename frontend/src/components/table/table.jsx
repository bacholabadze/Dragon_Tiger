import {useEffect, useRef, useState} from "react";
import "./index.css";


const Table = ({
  gameSpec,
  sendCard,
  card,
  handleChange,
  handleChangeBet,
  bet,
  sendBet,
  handleChangeTarget,
  target,
  sendTarget,
    tigerCard,
    dragonCard,
    socket,
    start_timestamp
}) => {
    console.log(start_timestamp)
    const [seconds, setSeconds]  = useState(15)
    const [renderBet, setRenderBets] = useState(true)
    const [dragonOn, setDragonOn] = useState(true)
    const [tigerOn, setTigerOn] = useState(false)

  useEffect(() => {
      if (seconds !== undefined) {
          let myInterval = setInterval(() => {
              if (seconds > 0) {
                  setSeconds(seconds - 1);
              }
              if (seconds === 0) {
                  clearInterval(myInterval)
                  setRenderBets(false)
              }
          }, 1000)
          return ()=> {
              clearInterval(myInterval);
          };
      }
    }, [seconds]);


    const handleClickOnBets = (e) => {
      const data = {
        amount: e.target.value,
        type: dragonOn ? "dragon" : "tiger"
      }
      socket.current.emit("place_bet", data)
    }

    const renderBets = () => {
      if (renderBet) {
        return (
            <>
            <div>
              <button value={1} onClick={handleClickOnBets}>1</button>
            </div>
          <div>
            <button value={5} onClick={handleClickOnBets}>5</button>
          </div>
          <div>
            <button value={10} onClick={handleClickOnBets}>10</button>
          </div>
        </>
        )
      }
    }
  const renderClickedButton = () => {
      if (dragonOn) {
        return (
            <div>
              <h1>Dragon</h1>
            </div>
        )
      } else {
        return (
            <div>
              <h1>Tiger</h1>
            </div>
        )
      }
  }

  return (
    <div className="cr">
      <div className="table">
        <h1>welcome to the table</h1>
        <p>min_bet: {gameSpec.min_bet || ""}</p>
        <p>max_bet: {gameSpec.max_bet || ""}</p>
        <form onSubmit={sendCard}>
          <input
            placeholder="Place Your Bets..."
            type="text"
            className="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChangeBet}
            value={bet}
          />
          <br />
          <input
            placeholder="place bets on dragon/tiger..."
            type="text"
            className="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChangeTarget}
            value={target}
          />
          <br />
          <input
            placeholder="Deal card..."
            type="text"
            className="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-sm"
            onChange={handleChange}
            value={card}
          />
          <button>Submit</button>
          {seconds}
        </form>
        <div>
          <h1>{dragonCard}</h1>
        </div>

        <div>
          <h1>{tigerCard}</h1>
        </div>
        <button onClick={e => {
          setDragonOn(true)
          setTigerOn(false)
        }}>Dragon</button>
        <button
            onClick={(e) => {
              setTigerOn(true)
              setDragonOn(false)
            }}
        >Tiger</button>
        {renderClickedButton()}
        {renderBets()}
      </div>
    </div>
  );
};

export default Table;
