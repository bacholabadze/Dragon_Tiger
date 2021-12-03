import "./App.css";

import { Route, Router } from "react-router-dom";
import Home from "./components/Home";
import Game from "./components/Game";

import route_history from "./router_history";

function App() {
  return (
    <Router history={route_history}>
      <div className="App">
        <Route path="/" exact component={Home} />
        <Route path="/game/:id" exact component={Game} />
      </div>
    </Router>
  );
}

export default App;
