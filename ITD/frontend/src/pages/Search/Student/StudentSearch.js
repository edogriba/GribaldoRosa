import React from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import SearchFilter from './SearchFilter';


const StudentSearch = () => {
    

    return (
        <div>
            <Navbar/>
            <div className="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16 mt-8 lg:mt-16">
                <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Your Search for an Internship starts here!</h2>
                <p className="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">Apply filters to suit your needs</p>
            </div> 
            <SearchFilter />
            <Footer />
        </div>

    );
};

export default StudentSearch;