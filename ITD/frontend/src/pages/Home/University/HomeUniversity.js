import React, {useEffect} from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import { useContext } from 'react';
import { UserContext } from '../../../context/UserContext';
import { useNavigate } from 'react-router-dom';

const HomeUniversity = () => {
    const { user, userLogout } = useContext(UserContext);   
    const navigate = useNavigate(); 
    useEffect(() => {
        if(user.type !== 'university') {
            navigate('/login');
        }
    }, [user]);
    console.log(user);
    return (
        <div>
            <Navbar  user={user} onLogout={userLogout}/>
            <section className="bg-white dark:bg-gray-900">
                <div className="py-8 px-4 mx-auto max-w-screen-xl sm:py-16 lg:px-6">
                    <div className="max-w-screen-md mb-8 lg:mb-16">
                        <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Welcome to the University Home Page</h2>
                        <p className="text-gray-500 sm:text-xl dark:text-gray-400">Ready to check on your students' internships?</p>
                    </div>
                    <div className="space-y-8 md:grid md:grid-cols-2 lg:grid-cols-3 md:gap-12 md:space-y-0">
                        <Link to="/universities/update">
                            <div>
                                <div className="flex justify-center items-center mb-4 w-10 h-10 rounded-full bg-primary-100 lg:h-12 lg:w-12 dark:bg-primary-900">
                                <svg className="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                                    <path fillRule="evenodd" d="M12 20a7.966 7.966 0 0 1-5.002-1.756l.002.001v-.683c0-1.794 1.492-3.25 3.333-3.25h3.334c1.84 0 3.333 1.456 3.333 3.25v.683A7.966 7.966 0 0 1 12 20ZM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10c0 5.5-4.44 9.963-9.932 10h-.138C6.438 21.962 2 17.5 2 12Zm10-5c-1.84 0-3.333 1.455-3.333 3.25S10.159 13.5 12 13.5c1.84 0 3.333-1.455 3.333-3.25S13.841 7 12 7Z" clipRule="evenodd"/>
                                </svg>
                                </div>
                                <h3 className="mb-2 text-xl font-bold dark:text-white">Update Your Information</h3>
                                <p className="text-gray-500 dark:text-gray-400">Keep your profile information up to date</p>
                            </div>
                        </Link>
                        <Link to="/universities/dashboard/profile">
                            <div>
                                <div className="flex justify-center items-center mb-4 w-10 h-10 rounded-full bg-primary-100 lg:h-12 lg:w-12 dark:bg-primary-900">
                                    <svg className="w-5 h-5 text-primary-600 lg:w-6 lg:h-6 dark:text-primary-300" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z" clipRule="evenodd"></path><path d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15c-2.796 0-5.487-.46-8-1.308z"></path></svg>                    
                                </div>
                                <h3 className="mb-2 text-xl font-bold dark:text-white">Students Internships</h3>
                                <p className="text-gray-500 dark:text-gray-400">Check the status of your students internships and track their progress.</p>
                            </div>
                        </Link>
                    </div>
                </div>
            </section>
            <Footer />
        </div>
    );
};

export default HomeUniversity;