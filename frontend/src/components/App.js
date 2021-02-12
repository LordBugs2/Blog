import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import HomePage from "./HomePage";
import CategoryPage from "./CategoryPage";
const App = () => {
  return (
    <Router>
      <div>
        <Route exact path="/">
          <div>
            <HomePage />
          </div>
        </Route>
        <Route path="/:category">
          <div>
            <CategoryPage />
          </div>
        </Route>
      </div>
    </Router>
  );
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);

export default App;
