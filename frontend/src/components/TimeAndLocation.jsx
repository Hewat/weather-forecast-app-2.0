import React from "react";

function TimeAndLocation({ weather_input }) {
  const { city, country, current_weather } = weather_input;

  return (
    <div>
      <div className="flex items-center justify-center my-6">
        <p className="text-white text-xl font-extralight">
          {`${current_weather.datetime.date} | Local time: ${current_weather.datetime.time}`}
        </p>
      </div>
      <div className="flex items-center justify-center my-3">
        <p className="text-white text-3xl font-medium">{`${city}, ${country}`}</p>
      </div>
    </div>
  );
}

export default TimeAndLocation;
