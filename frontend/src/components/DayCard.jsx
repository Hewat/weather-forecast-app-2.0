// @ts-nocheck
import React from "react";
import {
  UilArrowUp,
  UilArrowDown,
  UilInfoCircle,
} from "@iconscout/react-unicons";

function DayCard({ weekday, maxTemp, minTemp, handleClick }) {
  return (
    <div
      className="flex items-center justify-between py-4 px-4 bg-gray-900 rounded-lg text-white cursor-pointer mt-3"
      onClick={handleClick}
    >
      <p className="font-light">{weekday}</p>
      <div className="flex items-center space-x-2">
        <UilArrowUp size={18} className="mr-1" />
        <p className="font-light">High: {maxTemp}°C</p>
        <UilArrowDown size={18} className="ml-4 mr-1" />
        <p className="font-light">Low: {minTemp}°C</p>
      </div>
      <div className="flex justify-end">
        <UilInfoCircle size={24} className="hover:text-blue-500" />
        <p className="font-light">See details</p>
      </div>
    </div>
  );
}

export default DayCard;
