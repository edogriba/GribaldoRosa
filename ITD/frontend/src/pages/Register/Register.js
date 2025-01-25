import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';

const Register = () => {
  return (
    <div>
      <Navbar />
      <section className="bg-white dark:bg-gray-900">
        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
            <div className="mx-auto max-w-screen-md text-center mb-8 lg:mb-12">
                <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">
                    Choose how you would like to register
                </h2>
                <p className="mb-5 font-light text-gray-500 sm:text-xl dark:text-gray-400">
                    There are three types of users: student, company and university.
                </p>
            </div>
            <div className="flex flex-row justify-center gap-6">

                <div className="flex flex-col p-6 max-w-lg text-center text-gray-900 bg-white rounded-lg border border-gray-100 shadow dark:border-gray-600 xl:p-8 dark:bg-gray-800 dark:text-white">
                    <h3 className="mb-4 text-2xl font-semibold">Student</h3>
                    <p className="font-light text-gray-500 sm:text-lg dark:text-gray-400 mb-5">
                    Ready to take your career to the next level? Look for internship positions with this profile.
                    </p>
                    <Link to="/register/student" className="text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-primary-900">
                    Register as a Student
                    </Link>
                </div>

                <div className="flex flex-col p-6 max-w-lg text-center text-gray-900 bg-white rounded-lg border border-gray-100 shadow dark:border-gray-600 xl:p-8 dark:bg-gray-800 dark:text-white">
                    <h3 className="mb-4 text-2xl font-semibold">Company</h3>
                    <p className="font-light text-gray-500 sm:text-lg dark:text-gray-400 mb-5">
                    Looking for the best talents? Search no more, join S&C right now and connect with top applicants.
                    </p>
                    <Link to="/register/company" className="text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-primary-900">
                    Register as a Company
                    </Link>
                </div>

                <div className="flex flex-col p-6 max-w-lg text-center text-gray-900 bg-white rounded-lg border border-gray-100 shadow dark:border-gray-600 xl:p-8 dark:bg-gray-800 dark:text-white">
                    <h3 className="mb-4 text-2xl font-semibold">University</h3>
                    <p className="font-light text-gray-500 sm:text-lg dark:text-gray-400 mb-5">
                    Do you want to see the internships of your students and track their progress? Here is the right place.
                    </p>
                    <Link to="/register/university" className="text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:ring-primary-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-primary-900">
                    Register as a University
                    </Link>
                </div>
                </div>



        </div>
      </section>
      <Footer/>
    </div>
  );
};

export default Register;
