import React, { useState, useEffect } from 'react';
import { api } from '../../../api/api';
import SearchResults from './SearchResults';
import { toast } from 'react-hot-toast';

const SearchFilter = () => {
    // Filter values
    const [location, setLocation] = useState('');
    const [roleTitle, setRoleTitle] = useState('');
    const [company, setCompany] = useState('');
    const [minCompensation, setMinCompensation] = useState(0);
    const [duration, setDuration] = useState('');

    // Filters options
    const [companies, setCompanies] = useState([]);
    const [locations, setLocations] = useState([]);
    const [roleTitles, setRoleTitles] = useState([]);

    const [showResults, setShowResults] = useState(false);

    // Retrieved results
    const [positions, setPositions] = useState([]);

    const noFilterRequest = async () => {
        try {
            const res = await api.searchNoFilters();
            const data = await res.json();
            if (data.internships.length === 0) {
                toast.success('No positions found.');
            }
            setPositions(data.internships);
               
            setShowResults(true);
            
        }
        catch (error) {
            console.error('Error fetching applications:', error.message);
            alert('Failed to fetch applications. Please try again later.');
        };
    }

    const filterRequest = async () => {
        try {

            let minDuration = null;
            let maxDuration = null;

            switch (duration) {
                case '0-3':
                    minDuration = 0;
                    maxDuration = 3;
                    break;
                case '3-6':
                    minDuration = 3;
                    maxDuration = 6;
                    break;
                case '6-12':
                    minDuration = 6;
                    maxDuration = 12;
                    break;
                case '12+':
                    minDuration = 12;
                    maxDuration = null;
                    break;
                default:
                    minDuration = null;
                    maxDuration = null;
            }
            const filtersData = {};
            if (location) {
                filtersData.location = location;
            }
            if (company) {
                filtersData.companyName = company;
            }
            if (minCompensation) {
                filtersData.minStipend = parseInt(minCompensation);
            }
            if (minDuration !== null) {
                filtersData.minDuration = minDuration;
            }
            if (maxDuration !== null) {
                filtersData.maxDuration = maxDuration;
            }
            if (roleTitle) {
                filtersData.roleTitle = roleTitle;
            }
            const response = await api.searchFilters(filtersData);
            const data = await response.json();
            if (data.internships.length === 0) {
                toast.success('No positions found.');
            }
            setPositions(data.internships);
            setShowResults(true);

        }
        catch (error) {
            console.error('Error fetching applications:', error.message);
            alert('Failed to filter applications. Please try again later.');
        }   
    };

    useEffect(() => {
        const fetchFilters= async () => {
            try {
                const res = await api.getFilters();
                const data = await res.json();
                setLocations(data.locations);
                setCompanies(data.companiesNames);
                setRoleTitles(data.roleTitles);
            } catch (error) {
                console.error('Error fetching locations:', error.message);
                alert('Failed to load locations. Please try again later.');
            }
        };

        fetchFilters();
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
                        onChange={(e) => setRoleTitle(e.target.value)}
                    >
                        <option value="">All roles</option>
                        {roleTitles?.map((role) => (
                            <option key={role} value={role}>{role}</option>
                        ))}
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Location</label>
                    <select
                        value={location}
                        onChange={(e) => setLocation(e.target.value)}
                        className="mt-1 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg w-3/4 p-2.5"
                    >
                        <option value="">All locations</option>
                        {locations?.map((loc) => (
                            <option key={loc} value={loc}>{loc}</option>
                        ))}
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Companies</label>
                    <select 
                        onChange={(e) => setCompany(e.target.value)}
                        className="mt-1 block w-3/4 rounded-md border-gray-300 p-2"
                    >
                        <option value="">All companies</option>
                        {companies?.map((company) => (
                            <option key={company} value={company}>{company}</option>
                        ))}
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Duration (months)</label>
                    <select 
                        value={duration} 
                        onChange={(e) => setDuration(e.target.value)}
                        className="mt-1 block w-3/4 rounded-md border-gray-300 p-2"
                    >
                        <option value="">All durations</option>
                        <option value="0-3">0-3 months</option>
                        <option value="3-6">3-6 months</option>
                        <option value="6-12">6-12 months</option>
                        <option value="12+">12+ months</option>
                    </select>
                </div>
                <div className="mb-4 flex flex-col items-center">
                    <label className="block text-sm font-medium text-gray-700">Minimum Compensation</label>
                    <input 
                        type="range" 
                        min="0" max="3000" step="100" 
                        value={minCompensation} 
                        onChange={(e) => setMinCompensation(e.target.value)}
                        className="w-3/4 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer mt-5"
                    />
                    <p className="mt-2 text-sm text-gray-500">Selected: ${minCompensation}</p>
                </div>
            </div>
            <div className="flex justify-end mt-6">
                <button type="button" onClick={noFilterRequest} className="bg-secondary-600 text-white px-4 py-2 rounded-md mr-2">Browse All</button>
                <button type="submit" onClick={filterRequest} className="bg-primary-500 text-white px-4 py-2 rounded-md">Search</button>
            </div>
        {showResults && <SearchResults positions={positions} />}

        </div>
    );
};

export default SearchFilter;
