import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router";
import Header from "./Header";

const CategoryPage = () => {
  const { category } = useParams();
  const [items, setItems] = useState([]);
  const [query, setQuery] = useState(category);

  useEffect(() => {
    const fetchData = async () => {
      const x = await axios(
        `http://127.0.0.1:8000/api/get-categoryid-by-name?category=${query}`
      );
      const result = await axios(
        `http://127.0.0.1:8000/api/get-post-by-category?category=${x.data[0].id}`
      );

      setItems(result.data);
    };

    fetchData();
  }, []);

  const Posts = () => {
    return items.map((item) => {
      return (
        <div className="post" key={item.code}>
          <h1>{item.title}</h1>
          <a href={item.category}>{item.category}</a>
          <p>{item.content}</p>
          <br />
          <br />
        </div>
      );
    });
  };

  return (
    <div>
      <Header />
      <Posts />
    </div>
  );
};

export default CategoryPage;
