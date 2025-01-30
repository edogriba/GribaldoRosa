import React, { useState, useEffect } from 'react';
import { api } from '../../../api/api';

const SearchFilter = () => {
    const [location, setLocation] = useState('');
    const [companies, setCompanies] = useState([]);
    const [minCompensation, setMinCompensation] = useState(0);
    const [duration, setDuration] = useState('');
    const [locations, setLocations] = useState([]);
    const [roleTitles, setRoleTitles] = useState([]);

    const noFilterRequest = () => {
        try {
            console.log("No filter request");
            //const res = await api.getPositionListStudent();
        }
        catch (error) {
            console.error('Error fetching applications:', error.message);
            alert('Failed to fetch applications. Please try again later.');
        };
    }

    const filterRequest = () => {
        try {
            const data = {
                location,
                companies,
                minCompensation,
                duration,
            };
            console.log(data);
        }
        catch (error) {
            console.error('Error fetching applications:', error.message);
            alert('Failed to filter applications. Please try again later.');
        }   
    };

    useEffect(() => {
        const fetchLocations = async () => {
            try {
                // const res = await api.getLocationList();
                // const data = await res.json();
                // setLocations(data.locations);
                console.log("Fetching locations...");
            } catch (error) {
                console.error('Error fetching locations:', error.message);
                alert('Failed to load locations. Please try again later.');
            }
        };

        const fetchCompanies = async () => {
            try {
                // const res = await api.getCompanyList();
                // const data = await res.json();
                // setCompanies(data.companies);
                console.log("Fetching companies...");
            } catch (error) {
                console.error('Error fetching companies:', error.message);
                alert('Failed to load companies. Please try again later.');
            }
        };

        const fetchRoleTitles = async () => {
            try {
                // const res = await api.getRoleTitlesList();
                // const data = await res.json();
                // setCompanies(data.companies);
                console.log("Fetching role titles...");
            } catch (error) {
                console.error('Error fetching role title:', error.message);
                alert('Failed to load role titles. Please try again later.');
            }
        };
        fetchRoleTitles();
        fetchCompanies();
        fetchLocations();
    }, []);

    return (
        <div className="p-6">
            <div className="flex justify-start items-center mb-6">
                <h2 className="text-2xl font-semibold">Search Filters</h2>
            </div>
            <div className="grid grid-cols-3 gap-6">
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Role Titles</label>
                    <select  
                        className="mt-1 block w-3/4 rounded-md border-gray-300 p-2"
                    >
                        {roleTitles.map((role) => (
                            <option key={role.roleTitle} value={role.roleTitle}>{role.roleTitle}</option>
                        ))}
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Location</label>
                    <select
                        value={location}
                        onChange={(e) => setLocation(e.target.value)}
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg w-3/4 p-2.5"
                    >
                        <option value="" disabled>Select your location</option>
                        {locations.map((loc) => (
                            <option key={loc.id} value={loc.id}>{loc.name}</option>
                        ))}
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Companies</label>
                    <select 
                        multiple
                        onChange={(e) => setMinCompensation(e.target.value)}
                        className="mt-1 block w-3/4 rounded-md border-gray-300 p-2"
                    >
                        {companies.map((company) => (
                            <option key={company.id} value={company.id}>{company.name}</option>
                        ))}
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Duration (months)</label>
                    <input 
                        type="number" 
                        value={duration} 
                        onChange={(e) => setDuration(e.target.value)}
                        className="mt-1 block w-3/4 rounded-md border-gray-300 p-2"
                    />
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Minimum Compensation</label>
                    <input 
                        type="range" 
                        min="0" max="3000" step="100" 
                        value={minCompensation} 
                        onChange={(e) => setMinCompensation(e.target.value)}
                        className="w-3/4 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
                    />
                    <p className="mt-2 text-sm text-gray-500">Selected: ${minCompensation}</p>
                </div>
            </div>
            <div className="flex justify-end mt-6">
                <button type="button" onClick={noFilterRequest} className="bg-secondary-600 text-white px-4 py-2 rounded-md mr-2">Browse All</button>
                <button type="submit" onClick={filterRequest} className="bg-primary-500 text-white px-4 py-2 rounded-md">Apply</button>
            </div>
        </div>
    );
};

export default SearchFilter;
