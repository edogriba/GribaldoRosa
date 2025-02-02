import React, { useEffect, useState, useContext} from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../../../api/api";
import { toast } from "react-hot-toast";
import GoBack from "../../../components/GoBack";
import { UserContext } from "../../../context/UserContext";

const StudentPosition = () => {

    const { user } = useContext(UserContext);
    const [position, setPosition] = useState({});
    const { positionId } = useParams(); 
    const navigate = useNavigate(); 
    
    const handleApply = async () => {
        try {
            await api.createApplication({"internshipPositionId": parseInt(positionId)});
            navigate("/students/dashboard/applications");
        }
        catch (error) {
            console.log("Error closing position:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to close the position. Please try again later.");
        }
    }

    useEffect(() => {
        const fetchPosition = async () => {
            try {
                const res = await api.getPosition({"internshipPositionId": parseInt(positionId)}); 
                const data = await res.json();
                setPosition(data.internship_position);
                
            } catch (error) {
                console.log("Error fetching position:", error.message);
                if (error.status === 404) {
                    toast.error("Session expired please login again");
                    navigate("/login");
                }
                alert("Failed to load positions. Please try again later.");
            }
        };

        fetchPosition();
    }, [user]);

    return (
        <div>
            {/* Go Back Button */}
            <GoBack location="/students/search"/>
            <div className="max-w-4xl mx-auto p-6 bg-white  dark:bg-gray-800 dark:border-gray-700">
      
                {/* Header Section */}
                <div className="mb-6">
                    <h2 className="text-3xl font-bold text-gray-900 dark:text-white">
                    {position?.roleTitle || "Role Title"}
                    </h2>
                    <p className="text-lg text-gray-500 dark:text-gray-400">
                    {position?.programName || "Program Name"}
                    </p>
                </div>

                {/* Main Details Section */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Location
                    </p>
                    <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {position?.location || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Compensation
                    </p>
                    <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        ${position?.compensation || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Duration
                    </p>
                    <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {position?.duration || "Not specified"} months
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Status
                    </p>
                    <p
                        className={`inline-flex px-3 py-1 rounded-full text-sm font-medium ${
                        position?.status === "Open"
                            ? "bg-green-100 text-green-800"
                            : "bg-red-100 text-red-800"
                        }`}
                    >
                        {position?.status || "Unknown"}
                    </p>
                    </div>
                </div>

                {/* Additional Information Section */}
                <div className="space-y-4">
                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Benefits
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position?.benefits || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Languages Required
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position?.languagesRequired || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Skills Required
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position?.skillsRequired || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Description
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position?.description || "Not specified"}
                    </p>
                    </div>
                </div>

                {/* Footer Section */}

                <div className="mt-6 text-right">
                {position?.status === "Open" && (
                    <button
                    className="mx-2 px-6 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring focus:ring-primary-300"
                    onClick={handleApply} 
                    >
                    Apply to Position
                    </button>
                )}
                </div>
                
            </div>
        </div>
    );
};

export default StudentPosition;
