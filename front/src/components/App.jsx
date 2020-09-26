import React from "react";
import { Route, BrowserRouter as Router, Switch, Link } from "react-router-dom";
import Landing from "components/Landing";

export default function App() {
  return (
    <Router>
      <Switch>
        <Route path="/">
          <Landing />
        </Route>
      </Switch>
    </Router>
  );
}