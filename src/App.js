import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Home from "./pages/Home"
import './App.css';
import Album from "./pages/Advertisement"
import Login from "./pages/Login"

function App() {
  return (
    <Router>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/album" component={Album} />
      <Route exact path="/login" component={Login} />
    </Switch>
  </Router>
  );
}

export default App;
