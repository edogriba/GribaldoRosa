import React, { useEffect, useState, useContext} from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api } from "../../../api/api";
import { toast } from "react-hot-toast";
import GoBack from "../../../components/GoBack";
import { UserContext } from "../../../context/UserContext";
import Status from "../../../components/Status";
import ComplaintList from "../../Complaints/ComplaintList";

const StudentInternship = () => {
    const { user } = useContext(UserContext);
    const [internship, setInternship] = useState(null);
    const { internshipId } = useParams(); 
    const [complaints, setComplaints] = useState([]);
    const [showComplaints, setShowComplaints]= useState(false);
    const navigate = useNavigate();  

    const [showModal, setShowModal] = useState(false);

    const [content, setContent] = useState("");
    const [date, setDate] = useState("");


    if ( user.type !== "student") {
        navigate("/login");
    }

    const addComplaint = async () => {
        try {
            const complaint = {
                "internshipId": internshipId,
                "date": date,
                "content": content
            };
            const response = await api.addComplaint(complaint);
            const data = await response.json();
            if (data.type === "created") {
                toast.success("Complaint added successfully");
            }
            window.location.reload();
        }
        catch (error) {
            console.error("Error adding complaint:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to add complaint. Please try again later.");
        }
    }
    const fetchRelatedComplaints = async () => {   
            try {
                setShowComplaints(true);
                const res = await api.getInternship({"internshipId": parseInt(internshipId)}); // Use `positionId` directly
                const data = await res.json();

                if (res.type === "not_found") {
                    toast.error("No applications associated to this");
                }
                setComplaints(data.complaints);
    
                // Redirect to the Student dashboard
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

    const handleSubmit = async (e) => {
        e.preventDefault();
        setShowModal(false);
        await addComplaint();
    };


    useEffect(() => {
        const fetchInternship = async () => {
            try {
                const res = await api.getInternship({"internshipId": parseInt(internshipId)}); // Use `internshipId` directly
                const data = await res.json();
                setInternship(data);
                const companyId = data.company.id;
                const companyName = data.company.companyName;
                const studentId = data.student.id;
                const studentSurname = data.student.lastName;
                let transformedComplaints = data.complaints.map(complaint => {
                    if (complaint.sourceId === companyId) {
                      return { ...complaint, sourceId: companyName };
                    } else if (complaint.sourceId === studentId) {
                      return { ...complaint, sourceId: studentSurname };
                    } else {
                      return complaint;
                    }
                });
                setComplaints(transformedComplaints);            
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
            <GoBack location="/students/dashboard/internships"/>
            {internship && (
            <div className="max-w-4xl mx-auto p-6 bg-white  dark:bg-gray-800 dark:border-gray-700">
      
                {/* Header Section */}
                <div className="max-w-4xl mx-auto p-6 bg-white dark:bg-gray-800 dark:border-gray-700 rounded-lg shadow-lg">
                {/* Header Section */}
                <div className="mb-6 border-b pb-4">
                    <h2 className="text-3xl font-bold text-primary-700 dark:text-primary-400">
                    {internship.internshipPosition?.roleTitle || "Position Title"} - {internship.Student?.StudentName || "Student Name"}
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
                        <p className="mb-5 text-sm text-gray-400 dark:text-gray-500 uppercase">
                            Student CV
                        </p>
                        <a 
                            href={`/uploads/${internship.student?.id}/${internship.student?.CV}`}
                            download
                            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                        >
                            Download CV
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
                
                <button
                        className="mx-2 px-6 py-2 text-sm font-medium text-white bg-orange-600 rounded-lg hover:bg-orange-700 focus:outline-none focus:ring focus:ring-orange-300"
                        onClick={() => setShowModal(true)}
                    >
                        Add Complaint
                </button>

                    {showModal && (
                        <div className="fixed inset-0 flex items-center justify-center z-50">
                            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
                                <h2 className="text-2xl font-bold mb-4">Add Complaint</h2>
                                <form onSubmit={handleSubmit}>
                                    
                                    <div className="mb-4 relative max-w-sm">
                                    <input 
                                        type="date"
                                        id="complaintDate"
                                        value={date}
                                        max={new Date().toISOString().split("T")[0]}
                                        onChange={(e) => setDate(e.target.value)}
                                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                        placeholder="Select date"
                                        required
                                    />
                                    </div>
                                    <div className="mb-4">
                                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">Content</label>
                                        <textarea
                                            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300"
                                            value={content}
                                            onChange={(e) => setContent(e.target.value)}
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
                {showComplaints && (
                <div className="mt-6 text-right">
                    <ComplaintList complaints={complaints} />
                </div>
                )}
            </div>)}
        </div>
    );
};

export default StudentInternship;