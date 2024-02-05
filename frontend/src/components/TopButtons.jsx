import React from "react";

function TopButtons({ setCity }) {
  const cities = [
    {
      id: 1,
      title: "São Paulo",
    },
    {
      id: 2,
      title: "Toronto",
    },
    {
      id: 3,
      title: "Rio de Janeiro",
    },
    {
      id: 4,
      title: "Tokyo",
    },
    {
      id: 5,
      title: "Sidney",
    },
  ];

  return (
    <div className="flex items-center justify-around my-6">
      {cities.map((city) => (
        <button
          key={city.id}
          className="text-white text-lg font-medium"
          onClick={() => setCity(city.title)}
        >
          {city.title}
        </button>
      ))}
    </div>
  );
}

export default TopButtons;
