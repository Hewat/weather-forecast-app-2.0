const BASE_URL = "http://localhost:5000/search";

const getWeatherData = (city) => {
  const url = `${BASE_URL}?city=${city}`;

  console.log("URL:", url);

  return fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log("Data from service:", data);
      return data;
    })
    .catch((error) => {
      console.error(error);
      throw error;
    });
};

export default getWeatherData;
