import React from 'react';
import { useNavigate } from 'react-router-dom';

const GoBack = () => {
    const navigate = useNavigate();
    return (
        <button
        onClick={() => navigate(-1)} // Navigate to the previous page
        className="m-4 px-4 py-2 rounded bg-gray-800 text-white hover:bg-gray-700"
        >
        Go Back
        </button>
    )
}
export default GoBack;