import React, { useState } from "react";
// @ts-ignore
import { UilSearch } from "@iconscout/react-unicons";

function Inputs({ setCity }) {
  const [location, setLocation] = useState("");

  const handleSearchButton = () => {
    if (location) {
      setCity(location);
    }
  };

  return (
    <div className="flex flex-row justify-center my-6">
      <div className="flex flex-row items-center justify-center space-x-4">
        <input
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          type="text"
          placeholder="Search for a city"
          className="text-xl font-light p-2 w-full shadow-xl focus:outline-none capitalize placeholder:lowercase"
        />
        <UilSearch
          size={25}
          onClick={handleSearchButton}
          className="text-white cursor-pointer transition ease-out hover:scale-125"
        />
      </div>
    </div>
  );
}

export default Inputs;
