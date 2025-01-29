import React, { useState } from 'react';
import GoBack from '../../../components/GoBack';

const SearchFilter = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);

    const toggleModal = () => {
        setIsModalOpen(!isModalOpen);
    };

    return (
        <div>
            <GoBack />
            <div className="flex justify-center m-5">
                <button
                    className="block text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                    type="button"
                    onClick={toggleModal}
                >
                    Search
                </button>
            </div>
            {isModalOpen && (
                <div id="defaultModal" tabIndex="-1" aria-hidden="true" className="fixed top-0 left-0 right-0 z-50 w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-modal md:h-full">
                    <div className="fixed inset-0 flex items-center justify-center z-50">
                        <div className="bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
                            <h2 className="text-xl font-semibold mb-4">Search Filters</h2>
                            <div className="mb-4">
                                <label className="block text-sm font-medium text-gray-700">Position Type</label>
                                <select className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                                    <option>Full-time</option>
                                    <option>Part-time</option>
                                    <option>Internship</option>
                                </select>
                            </div>
                            <div className="mb-4">
                                <label className="block text-sm font-medium text-gray-700">Location</label>
                                <input type="text" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500" />
                            </div>
                            <div className="mb-4">
                                <label className="block text-sm font-medium text-gray-700">Duration (months)</label>
                                <input type="number" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500" />
                            </div>
                            <div className="mb-4">
                                <label className="block text-sm font-medium text-gray-700">Pay</label>
                                <input type="number" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500" />
                            </div>
                            <div className="mb-4">
                                <label className="block text-sm font-medium text-gray-700">Industry</label>
                                <select className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                                    <option>Technology</option>
                                    <option>Finance</option>
                                    <option>Healthcare</option>
                                    <option>Education</option>
                                </select>
                            </div>
                            <div className="flex justify-end">
                                <button type="button" className="bg-secondary-700 text-white px-4 py-2 rounded-md mr-2" onClick={toggleModal}>Cancel</button>
                                <button type="submit" className="bg-primary-500 text-white px-4 py-2 rounded-md">Apply</button>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default SearchFilter;