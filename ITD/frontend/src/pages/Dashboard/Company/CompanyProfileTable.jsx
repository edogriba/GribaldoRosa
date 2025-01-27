import React, { useContext } from 'react';
import { UserContext } from '../../../context/UserContext';

const CompanyProfileTable = ({ company }) => {
    const { user } = useContext(UserContext);

    return (
        <section className="bg-gray-50 dark:bg-gray-900 p-6 sm:p-8">
            <div className="mx-auto max-w-screen-xl px-6 lg:px-16">
                <div className="bg-white dark:bg-gray-800 relative shadow-md sm:rounded-lg overflow-hidden">
                    <div className="overflow-x-auto">
                        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                            <thead className="text-xs text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th className="px-6 py-3">Description</th>
                                    <th className="px-6 py-3">Email</th>
                                    <th className="px-6 py-3">Location</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                    <td className="px-6 py-4">{user.description}</td>
                                    <td className="px-6 py-4">{user.email}</td>
                                    <td className="px-6 py-4">{user.location}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default CompanyProfileTable;
