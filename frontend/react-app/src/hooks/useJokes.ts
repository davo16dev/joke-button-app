import { useState } from "react";

// Custom hook to fetch jokes
const useJokes = () => {
  const [jokes, setJokes] = useState<string[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const getJoke = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch("http://localhost:8080/joke");
      if (!response.ok) {
        throw new Error("Failed to fetch joke");
      }
      const data = await response.json();
      setJokes((prevJokes) => [data.joke, ...prevJokes]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setLoading(false);
    }
  };

  // Return the values and the function to fetch a joke
  return { jokes, loading, error, getJoke };
};

export default useJokes;
