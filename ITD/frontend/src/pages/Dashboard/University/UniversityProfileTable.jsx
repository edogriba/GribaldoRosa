import React, { useContext } from 'react';
import { UserContext } from '../../../context/UserContext';

const UniversityProfileTable = () => {
    const { user } = useContext(UserContext);

    return (
        <section className="flex justify-center items-center dark:bg-gray-900 p-6 sm:p-8">
            <div className="mx-auto max-w-screen-xl px-6 lg:px-16">
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <div className="bg-white dark:bg-gray-800 relative sm:rounded-lg overflow-hidden">
                        <div className="overflow-x-auto">
                            <table className="w-full text-sm text-left border-y-0 text-gray-500 dark:text-gray-400">
                                <tbody>
                                    <tr className="bg-white border dark:bg-gray-800 dark:border-gray-700">
                                        <th className="px-6 py-3 text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">Description</th>
                                        <td className="px-6 py-4">{user.description}</td>
                                    </tr>
                                    <tr className="h-10 text-white">
                                        <th className="text-white px-6 py-3">--------------</th>
                                        <td className="text-white px-6 py-4">-----------------</td>
                                    </tr> 
                                    <tr className="bg-white border dark:bg-gray-800 dark:border-gray-700">
                                        <th className="px-6 py-3 text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">Website</th>
                                        <td className="px-6 py-4">
                                            <a href={user.websiteURL} className="text-blue-600 dark:text-blue-400" target="_blank" rel="noopener noreferrer">
                                                {user.websiteURL}
                                            </a>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div className="bg-white dark:bg-gray-800 relative sm:rounded-lg overflow-hidden">
                        <div className="overflow-x-auto">
                            <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                                <tbody>
                                    <tr className="bg-white border dark:bg-gray-800 dark:border-gray-700">
                                        <th className="px-6 py-3 text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">Email</th>
                                        <td className="px-6 py-4">{user.email}</td>
                                    </tr>
                                    <tr className="h-10 text-white">
                                        <th className="text-white px-6 py-3">--------------</th>
                                        <td className="text-white px-6 py-4">-----------------</td>
                                    </tr> 
                                    <tr className="bg-white border dark:bg-gray-800 dark:border-gray-700">
                                        <th className="px-6 py-3 text-gray-700 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400">Address</th>
                                        <td className="px-6 py-4">{user.address}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default UniversityProfileTable;
