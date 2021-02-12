import React from "react";
import "./SearchBar.css";
import SearchIcon from "@material-ui/icons/Search";

const SearchBar = () => {
  const getValueFromInput = () => {
    let value = document.getElementsByName("category")[0].value;
    location.assign(`http://127.0.0.1:8000/${value}`);
  };
  return (
    <div>
      <div className="search-bar">
        <input
          className="input"
          type="text"
          placeholder="Category"
          name="category"
        />
        <br />
        <br />
        <button type="submit" onClick={getValueFromInput}>
          <SearchIcon />
        </button>
        <br />
        <br />
        <br />
      </div>
    </div>
  );
};

export default SearchBar;
