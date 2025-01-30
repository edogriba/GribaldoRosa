import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../../../api/api";
import { toast } from "react-hot-toast";
import GoBack from "../../../components/GoBack";
import CompanyPositionApplications from "./CompanyPositionApplications";

const CompanyPosition = () => {
    const [position, setPosition] = useState({});
    const { positionId } = useParams(); // Extract the dynamic `positionId` from the route
    const navigate = useNavigate(); // Hook to navigate programmatically
    const [applications, setApplications] = useState([]);
    const [showPosition, setShowPosition]= useState(false);
    

    const handleClosePosition = async () => {   
        try {
            console.log("Closing Position...", positionId); // Debug log
            const res = await api.closePosition({"internshipPositionId": positionId}); // Use `positionId` directly
            const data = await res.json();
            console.log("Closed Position:", data); // Debug log
            if (data.type === "success") {
                toast.success("Internship was closed successfully");
            }
            // Redirect to the company dashboard
            navigate("/companies/dashboard/positions");
        }
        catch (error) { 
            console.error("Error closing position:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to close the position. Please try again later.");
        }
    }

    const fetchRelatedApplications = async () => {   
        try {
            console.log("Fetching applications...", positionId); // Debug log
            setShowPosition(true);
            console.log("Fetching Applications..."); // Debug log
            const res = await api.getApplicationListCompany({"internshipPositionId": positionId}); // Use `positionId` directly
            const data = await res.json();
            console.log("Qui")
            if (res.type === "not_found") {
                toast.error("No applications associated to this");
            }
            console.log("Applications fetched:", data.applications); // Debug log
            setApplications(data.applications);

            // Redirect to the company dashboard
            //navigate(`/companies/dashboard/positions/${positionId}/applications`);
        }
        catch (error) { 
            console.error("Fetching applications:", error.message);
            if (error.status === 401) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to fetch the applications of the position. Please try again later.");
        }
    }

    const hideRelatedApplications = () => { 

        setShowPosition(false);
    }

    useEffect(() => {
        const fetchPosition = async () => {
            try {
                //console.log("Fetching Position...", useParams()); // Debug log
                console.log("Fetched Position Id:", positionId); // Debug log
                const res = await api.getPosition({"internshipPositionId": positionId}); // Use `positionId` directly
                const data = await res.json();
                console.log("Fetched Position:", data); // Debug log

                console.log("Fetched Position:", data.internship_position); // Debug log
                setPosition(data.internship_position);
                
            } catch (error) {
                console.error("Error fetching position:", error.message);
                if (error.status === 404) {
                    toast.error("Session expired please login again");
                    navigate("/login");
                }
                alert("Failed to load positions. Please try again later.");
            }
        };

        fetchPosition();
    }, [positionId]);

    return (
        <div>
            {/* Go Back Button */}
            <GoBack />
            <div className="max-w-4xl mx-auto p-6 bg-white  dark:bg-gray-800 dark:border-gray-700">
      
                {/* Header Section */}
                <div className="mb-6">
                    <h2 className="text-3xl font-bold text-gray-900 dark:text-white">
                    {position.roleTitle || "Role Title"}
                    </h2>
                    <p className="text-lg text-gray-500 dark:text-gray-400">
                    {position.programName || "Program Name"}
                    </p>
                </div>

                {/* Main Details Section */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Location
                    </p>
                    <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {position.location || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Compensation
                    </p>
                    <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        ${position.compensation || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Duration
                    </p>
                    <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {position.duration || "Not specified"} months
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Status
                    </p>
                    <p
                        className={`inline-flex px-3 py-1 rounded-full text-sm font-medium ${
                        position.status === "Open"
                            ? "bg-green-100 text-green-800"
                            : "bg-red-100 text-red-800"
                        }`}
                    >
                        {position.status || "Unknown"}
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
                        {position.benefits || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Languages Required
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position.languagesRequired || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Skills Required
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position.skillsRequired || "Not specified"}
                    </p>
                    </div>

                    <div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                        Description
                    </p>
                    <p className="text-base text-gray-800 dark:text-gray-200">
                        {position.description || "Not specified"}
                    </p>
                    </div>
                </div>

                {/* Footer Section */}

                <div className="mt-6 text-right">
                {position.status === "Open" && (
                    <button
                    className="mx-2 px-6 py-2 text-sm font-medium text-white bg-red-600 rounded-lg hover:bg-red-700 focus:outline-none focus:ring focus:ring-red-300"
                    onClick={handleClosePosition} 
                    >
                    Close Position
                    </button>
                )}
                {!showPosition && (
                    <button
                    className="mx-2 px-6 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring focus:ring-primary-300"
                    onClick={fetchRelatedApplications} 
                    >
                    See Related Applications
                    </button>
                )}
                {showPosition && (
                    <button
                    className="mx-2 px-6 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring focus:ring-primary-300"
                    onClick={hideRelatedApplications} 
                    >
                    Hide Applications
                    </button>
                )}
                </div>
                
                {/* Optional Rendering Application Section */}
                {showPosition && (
                    <div>
                        
                        <CompanyPositionApplications applications={applications} />
                    </div>
                )}
            </div>
        </div>
    );
};

export default CompanyPosition;
