import React, { useEffect, useState, useContext} from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../../../api/api";
import { toast } from "react-hot-toast";
import GoBack from "../../../components/GoBack";
import { UserContext } from "../../../context/UserContext";
import Status from "../../../components/Status";

const UniversityInternship = () => {
    const { user } = useContext(UserContext);
    const [internship, setInternship] = useState(null);
    const { internshipId } = useParams(); 
    const [complaints, setComplaints] = useState([]);
    const [showComplaints, setShowComplaints]= useState(false);
    const navigate = useNavigate();  

    const fetchRelatedComplaints = async () => {   
            try {
                console.log("Fetching complaints"); // Debug log
                setShowComplaints(true);
                console.log("Fetching Applications..."); // Debug log
                const res = await api.getComplaints({"internshipId": parseInt(internshipId)}); // Use `positionId` directly
                const data = await res.json();

                if (res.type === "not_found") {
                    toast.error("No applications associated to this");
                }
                console.log("Complaints fetched:", data.complaints); // Debug log
                setComplaints(data.complaints);
    
                // Redirect to the University dashboard
                //navigate(`/companies/dashboard/positions/${positionId}/applications`);
            }
            catch (error) { 
                console.error("Fetching complaints:", error.message);
                if (error.status === 401) {
                    toast.error("Session expired please login again");
                    navigate("/login");
                }
                alert("Failed to fetch the complaints of the internship. Please try again later.");
            }
        }
    
        const hideRelatedComplaints = () => { 
    
            setShowComplaints(false);
        }

    useEffect(() => {
        const fetchInternship = async () => {
            try {
                //console.log("Fetching Internship...", useParams()); // Debug log
                console.log("Fetched Internship Id:", internshipId); // Debug log
                const res = await api.getInternship({"internshipId": parseInt(internshipId)}); // Use `internshipId` directly
                const data = await res.json();
                console.log("Fetched Internship:", data); // Debug log
                setInternship(data);
                console.log("Fetched Internship:", data.internship); // Debug log
            
                
            } catch (error) {
                console.error("Error fetching internship:", error.message);
                if (error.status === 404) {
                    toast.error("Session expired please login again");
                    navigate("/login");
                }
                alert("Failed to load internships. Please try again later.");
            }
        };

        fetchInternship();
    }, [user]);

    return (
        <div>
            {/* Go Back Button */}
            <GoBack location="/universities/dashboard/internships"/>
            {internship && (
            <div className="max-w-4xl mx-auto p-6 bg-white  dark:bg-gray-800 dark:border-gray-700">
      
                {/* Header Section */}
                <div className="max-w-4xl mx-auto p-6 bg-white dark:bg-gray-800 dark:border-gray-700 rounded-lg shadow-lg">
                {/* Header Section */}
                <div className="mb-6 border-b pb-4">
                    <h2 className="text-3xl font-bold text-primary-700 dark:text-primary-400">
                    {internship.internshipPosition?.roleTitle || "Position Title"} - {internship.company?.companyName || "Company Name"}
                    </h2>
                    <p className="text-lg text-gray-500 dark:text-gray-400">
                        {internship.internshipPosition?.programName || "Program Name"}
                    </p>
                </div>
                {/* Position Details Header */}
                <div className="mb-6 border-b pb-4">
                    <h3 className="text-2xl font-semibold text-primary-700 dark:text-primary-400">
                        Position Details
                    </h3>
                    <p className="text-md text-gray-500 dark:text-gray-400">
                        Below are the details of the internship position.
                    </p>
                </div>
                {/* Position Details Section */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Location
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                            {internship.internshipPosition?.location || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Compensation
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                            ${internship.internshipPosition?.compensation || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Duration
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                            {internship.internshipPosition?.duration || "Not specified"} months
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <Status status={internship.internship?.status} />
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Skills Required
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {internship.internshipPosition?.skillsRequired || "Not specified"}
                        </p>
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Description
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {internship.internshipPosition?.description || "Not specified"}
                        </p>
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Languages Required
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {internship.internshipPosition?.languagesRequired || "Not specified"}
                        </p>
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Benefits
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {internship.internshipPosition?.benefits || "Not specified"}
                        </p>
                    </div>
                </div>
                {/* Candidate Details Header */}
                <div className="mb-6 border-b pb-4">
                    <h3 className="text-2xl font-semibold text-primary-700 dark:text-primary-400">
                        Candidate Details
                    </h3>
                    <p className="text-md text-gray-500 dark:text-gray-400">
                        Below are the candidate's details.
                    </p>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student Name
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.firstName} {internship.student?.lastName}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student Email
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.email}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student Degree Program
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.degreeProgram}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student GPA
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.GPA || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Location
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.location || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Phone Number
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.phoneNumber || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Graduation Year
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {internship.student?.graduationYear || "Not specified"}
                        </p>
                    </div>


                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student CV
                        </p>
                        <a
                            href={internship.student?.CV}
                            className="text-primary-600 hover:underline"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            View CV
                        </a>
                    </div>
                </div>
                </div>

                {/* Footer Section */}

                <div className="mt-6 text-right">
                    
                {!showComplaints && (
                    <button
                    className="mx-2 px-6 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring focus:ring-primary-300"
                    onClick={fetchRelatedComplaints} 
                    >
                    See Complaints
                    </button>

                )}
                {showComplaints && (
                    <button
                    className="mx-2 px-6 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring focus:ring-primary-300"
                    onClick={hideRelatedComplaints} 
                    >
                    Hide Complaints
                    </button>
                )}
                </div>
            </div>)}
        </div>
    );
};

export default UniversityInternship;