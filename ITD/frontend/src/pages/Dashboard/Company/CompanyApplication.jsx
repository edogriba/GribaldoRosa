import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../../../api/api";
import { toast } from "react-hot-toast";
import GoBack from "../../../components/GoBack";
import Status from "../../../components/Status";

const CompanyApplication = () => {
    const [application, setApplication] = useState({});
    const { applicationId, positionId } = useParams();
    const [showModal, setShowModal] = useState(false) // Extract the dynamic `applicationId` from the route
    const [date, setDate] = useState("");
    const [link, setLink] = useState("");
    const navigate = useNavigate(); // Hook to navigate programmatically

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response  = await api.createAssessment({"applicationId": parseInt(applicationId), "date": date, "link": link}); // Use `applicationId` directly
            const data = await response.json();
            if (data.type === 'created') {
                toast.success("Assessment added successfully");
                setShowModal(false);
            }
        }
        catch (error) {
            console.error("Error assessing application:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to assess the application. Please try again later.");
        }
    }
    const handleAccept = async () => {
        try {
            const res = await api.acceptApplication({"applicationId": parseInt(applicationId), "internshipPositionId": parseInt(positionId)}); // Use `applicationId` directly
            const data = await res.json();
            setApplication(data);
            navigate(`/companies/dashboard/positions/${positionId}`);
        }
        catch (error) { 
            console.error("Error acceptin application:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to accept the application. Please try again later.");
        }
    }
    const handleReject = async () => {
        try {
            const res = await api.rejectApplication({"applicationId": parseInt(applicationId), "internshipPositionId": parseInt(positionId)}); // Use `applicationId` directly
            const data = await res.json();
            setApplication(data);
            navigate(`/companies/dashboard/positions/${positionId}`);
        }
        catch (error) { 
            console.error("Error rejecting position:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to reject the application. Please try again later.");
        }
    }
    useEffect(() => {
        const fetchApplication = async () => {
            try {
                const res = await api.getApplicationCompany({"applicationId": applicationId}); // Use `applicationId` directly
                const data = await res.json();
                setApplication(data); // Assuming the API returns the entire application object
            } catch (error) {
                console.error("Error fetching application:", error.message);
                if (error.status === 404) {
                    toast.error("Session expired please login again");
                    navigate("/login");
                }
                alert("Failed to load application details. Please try again later.");
            }
        };
        fetchApplication();
    }, [applicationId, navigate]);

    return (
        <div>
            {/* Go Back Button */}
            <GoBack location={`/companies/dashboard/positions/${positionId}`}/>
            <div className="max-w-4xl mx-auto p-6 bg-white dark:bg-gray-800 dark:border-gray-700 rounded-lg shadow-lg">
                {/* Header Section */}
                <div className="mb-6 border-b pb-4">
                    <h2 className="text-3xl font-bold text-primary-700 dark:text-primary-400">
                    {application.internshipPosition?.roleTitle || "Position Title"} - {application.company?.companyName || "Company Name"}
                    </h2>
                    <p className="text-lg text-gray-500 dark:text-gray-400">
                        {application.internshipPosition?.programName || "Program Name"}
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
                            {application.internshipPosition?.location || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Compensation
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                            ${application.internshipPosition?.compensation || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Duration
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                            {application.internshipPosition?.duration || "Not specified"} months
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <Status status={application.application?.status} />
                    {application.application?.status === "Assessed" ? (<div><div>Assessment date: {application.assessment.date} </div> <div>Link: <a className="underline" href={`${application.assessment.link}`} >{application.assessment.link}</a></div></div>) : ( <div></div>)}
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Skills Required
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {application.internshipPosition?.skillsRequired || "Not specified"}
                        </p>
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Description
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {application.internshipPosition?.description || "Not specified"}
                        </p>
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Languages Required
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {application.internshipPosition?.languagesRequired || "Not specified"}
                        </p>
                    </div>
                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Benefits
                        </p>
                        <p className="text-lg font-medium text-gray-800 dark:text-gray-200">
                        {application.internshipPosition?.benefits || "Not specified"}
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
                            {application.student?.firstName} {application.student?.lastName}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student Email
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {application.student?.email}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student Degree Program
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {application.student?.degreeProgram}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student GPA
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {application.student?.GPA || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Location
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {application.student?.location || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Phone Number
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {application.student?.phoneNumber || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Graduation Year
                        </p>
                        <p className="text-base text-gray-800 dark:text-gray-200">
                            {application.student?.graduationYear || "Not specified"}
                        </p>
                    </div>

                    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                        <p className="mb-5 text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student CV
                        </p>
                        <a 
                            href={`/uploads/${application.student?.id}/${application.student?.CV}`}
                            download
                            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                        >
                            Download CV
                        </a>
                    </div>
                </div>
                {/* Action Buttons */}
                { (application.application?.status === "Pending" || application.application?.status === "Assessed")  &&
                <div className="flex justify-end mt-6 space-x-4">
                    <button
                        onClick={handleAccept}
                        className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
                    >
                        Accept
                    </button>
                    <button
                        onClick={handleReject}
                        className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700"
                    >
                        Reject
                    </button>
                    <button
                        onClick={() => setShowModal(true)}
                        className="px-4 py-2 bg-yellow-300 text-white rounded-lg hover:bg-yellow-500"
                    >
                        Assess
                    </button>
                    {showModal && (
                        <div className="fixed inset-0 flex items-center justify-center z-50">
                            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
                                <h2 className="text-2xl font-bold mb-4">Create Virtual Assessment Meeting</h2>
                                <form onSubmit={handleSubmit}>
                                    
                                    <div className="mb-4 relative max-w-sm">
                                    <input 
                                        type="date"
                                        id="complaintDate"
                                        value={date}
                                        min={new Date().toISOString().split("T")[0]}
                                        onChange={(e) => setDate(e.target.value)}
                                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="Select date"
                                        required
                                    />
                                    </div>
                                    <div className="mb-4">
                                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">Link for the Virtual Assessment</label>
                                        <textarea
                                            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300"
                                            value={link}
                                            onChange={(e) => setLink(e.target.value)}
                                            required
                                        />
                                    </div>
                                    <div className="flex justify-end">
                                        <button
                                            type="button"
                                            className="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-lg hover:bg-gray-300 focus:outline-none focus:ring focus:ring-gray-300"
                                            onClick={() => setShowModal(false)}
                                        >
                                            Cancel
                                        </button>
                                        <button
                                            type="submit"
                                            className="px-4 py-2 text-sm font-medium text-white bg-primary-600 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring focus:ring-primary-300"
                                        >
                                            Submit
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    )}
                </div>
                }   
            </div>
        </div>
    );
};

export default CompanyApplication;
