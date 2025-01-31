import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../../../api/api";
import { toast } from "react-hot-toast";
import GoBack from "../../../components/GoBack";
import Status from "../../../components/Status";

const StudentApplication = () => {
    const [application, setApplication] = useState({});
    const { applicationId } = useParams(); // Extract the dynamic `applicationId` from the route
    const navigate = useNavigate(); // Hook to navigate programmatically

    useEffect(() => {
        const fetchApplication = async () => {
            try {
                console.log("Fetched applicationId:", applicationId); // Debug log
                const res = await api.getApplicationStudent({"applicationId": applicationId}); // Use `applicationId` directly
                const data = await res.json();
                console.log("Fetched Application:", data); // Debug log
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
    }, [applicationId]);

    return (
        <div>
            {/* Go Back Button */}
            <GoBack location="/students/dashboard/applications/"/>
            <div className="max-w-4xl mx-auto p-6 bg-white dark:bg-gray-800 dark:border-gray-700 rounded-lg shadow-lg">
                {/* Header Section */}
                <div className="mb-6 border-b pb-4">
                    <h2 className="text-3xl font-bold text-primary-700 dark:text-primary-400">
                        Application Details
                    </h2>
                    <p className="text-lg text-gray-500 dark:text-gray-400">
                        {application.internshipPosition?.roleTitle || "Position Title"} - {application.company?.companyName || "Company Name"}
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
                {/* Main Details Section */}
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
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Status
                        </p>
                       <Status status={application.application?.status}/>
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
                {/* Additional Information Section */}
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
                        <p className="text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student CV
                        </p>
                        <a
                            href={application.student?.CV}
                            className="text-primary-600 hover:underline"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            View CV
                        </a>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default StudentApplication;
