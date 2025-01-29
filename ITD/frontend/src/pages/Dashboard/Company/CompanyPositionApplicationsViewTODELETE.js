import React, { use, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import GoBack from '../../../components/GoBack';
import { toast } from 'react-hot-toast';
import { api } from '../../../api/api';

const CompanyPositionApplicationsView = (positionId) => {
    const navigate = useNavigate();
    const fetchApplications = async () => {
        try {
            console.log("Fetching Applications..."); // Debug log
            const res = await api.getApplicationListCompany({"internshipPositionId": positionId}); // Use `positionId` directly
            const data = await res.json();
            console.log("Fetched Applications:", data); // Debug log
            
        }
        catch (error) { 
            console.error("Error fetching applications:", error.message);
            if (error.status === 404) {
                toast.error("Session expired please login again");
                navigate("/login");
            }
            alert("Failed to fetch applications. Please try again later.");
        }
    }
    useEffect(() => {
        fetchApplications();
    }, []);
    return (
        <div>
            <h1>Company Position Applications</h1>
            <GoBack />
        </div>
    )

}

export default CompanyPositionApplicationsView;