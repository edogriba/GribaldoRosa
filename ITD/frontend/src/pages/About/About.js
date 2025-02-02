import React from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import { useContext } from 'react';
import { UserContext } from '../../context/UserContext';
const About = () => {
    const { user, userLogout } = useContext(UserContext);
    return (
        <div>
            <Navbar user={user} onLogout={userLogout}/>
            <div className="container mx-auto p-4">
                <div className="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">S&C (Students & Companies)</h2>
                <p className="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">                S&C is a startup founded at Politecnico di Milano that offers an innovative web application for students to look for internships and for companies to offer internships. It helps track the progress of undertaken internships and lets universities monitor their students' internship progress as well.</p>
                </div> 

                <div className="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Story</h2>
                <p className="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">It all began with a Software Engineering 2 assignment!</p>
                </div> 
                <ol className="relative border-l border-gray-200 dark:border-gray-700">
                    <li className="mb-10 ms-4">
                        <div className="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                        <time className="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">October 2024</time>
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Foundation</h3>
                        <p className="text-base font-normal text-gray-500 dark:text-gray-400">
                            Edoardo and Federico, two students from Politecnico di Milano, founded S&C with the vision to bridge the gap between students and companies.
                        </p>
                    </li>
                    <li className="mb-10 ms-4">
                        <div className="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                        <time className="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">Febraury 2025</time>
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Launch</h3>
                        <p className="text-base font-normal text-gray-500 dark:text-gray-400">
                            The S&C platform was launched, providing a seamless experience for students to find internships and for companies to offer them.
                        </p>
                    </li>
                    <li className="mb-10 ms-4">
                        <div className="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                        <time className="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">March 2025 - Now</time>
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Growth</h3>
                        <p className="text-base font-normal text-gray-500 dark:text-gray-400">
                            S&C expanded its services, allowing universities to monitor their students' internship progress, ensuring a comprehensive internship experience.
                        </p>
                    </li>
                </ol>
                <h2 className="text-3xl font-semibold mb-4">Our Founders</h2>
                <section className="bg-white dark:bg-gray-900">
                    <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6 ">
                        <div className="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                            <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Team</h2>
                            <p className="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">The students who made the web app possible</p>
                        </div> 
                        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">

                        <div className="grid gap-8 mb-6 lg:mb-16 md:grid-cols-2">
                            <div className="items-center bg-gray-50 rounded-lg shadow sm:flex dark:bg-gray-800 dark:border-gray-700">
                            <span>
                                <img
                                className="object-cover w-80 h-48 rounded-lg sm:rounded-none sm:rounded-l-lg"
                                src="/edogriba.jpg"
                                alt="Edoardo Gribaldo"
                                />
                            </span>
                            <div className="p-5">
                                <h3 className="text-xl font-bold tracking-tight text-gray-900 dark:text-white">
                                Edoardo Gribaldo
                                </h3>
                                <span className="text-gray-500 dark:text-gray-400">Co-Founder</span>
                                <p className="mt-3 mb-4 font-light text-gray-500 dark:text-gray-400">
                                Edoardo is passionate about computer science and creating this startup was a dream come true for him.
                                </p>
                                <ul className="flex space-x-4 sm:mt-0">
                                <li>
                                    <a href="https://github.com/edogriba">
                                    <span className="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        {/* GitHub SVG icon */}
                                    </span>
                                    </a>
                                </li>
                                <li>
                                    <a href="https://linkedin.com/edogriba">
                                    <span className="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        {/* LinkedIn SVG icon */}
                                    </span>
                                    </a>
                                </li>
                                </ul>
                            </div>
                            </div>
                            <div className="items-center bg-gray-50 rounded-lg shadow sm:flex dark:bg-gray-800 dark:border-gray-700">
                            <span>
                                <img
                                className="object-cover w-80 h-48 rounded-lg sm:rounded-none sm:rounded-l-lg"
                                src="/fede.jpeg"
                                alt="Federico Rosa"
                                />
                            </span>
                            <div className="p-5">
                                <h3 className="text-xl font-bold tracking-tight text-gray-900 dark:text-white">
                                Federico Rosa
                                </h3>
                                <span className="text-gray-500 dark:text-gray-400">Co-Founder</span>
                                <p className="mt-3 mb-4 font-light text-gray-500 dark:text-gray-400">
                                Federico loves Computer Science and this startup was a great chance to put to work his ideas.
                                </p>
                                <ul className="flex space-x-4 sm:mt-0">
                                <li>
                                    <a href="https://github.com/Thalamicks">
                                    <span className="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        {/* GitHub SVG icon */}
                                    </span>
                                    </a>
                                </li>
                                </ul>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </section>
                <div className="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                    <h2 className="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Success Stories</h2>
                </div> 
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <section className="bg-white dark:bg-gray-900">
                        <div className="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-16 lg:px-6">
                            <figure className="max-w-screen-md mx-auto">
                                <svg className="h-12 mx-auto mb-3 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor"/>
                                </svg> 
                                <blockquote>
                                    <p className="text-2xl font-medium text-gray-900 dark:text-white">"Thanks to S&C, I found an amazing internship at a top tech company. The platform made the process so easy and efficient!"</p>
                                </blockquote>
                                <figcaption className="flex items-center justify-center mt-6 space-x-3">
                                    <img className="w-6 h-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/jese-leos.png" alt="profile"/>
                                    <div className="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
                                        <div className="pr-3 font-medium text-gray-900 dark:text-white">Marco</div>
                                    </div>
                                </figcaption>
                            </figure>
                        </div>
                    </section>
                    <section className="bg-white dark:bg-gray-900">
                        <div className="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-16 lg:px-6">
                            <figure className="max-w-screen-md mx-auto">
                                <svg className="h-12 mx-auto mb-3 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor"/>
                                </svg> 
                                <blockquote>
                                    <p className="text-2xl font-medium text-gray-900 dark:text-white">"S&C connected us with talented students who have become valuable members of our team. It's a fantastic resource for finding interns."</p>
                                </blockquote>
                                <figcaption className="flex items-center justify-center mt-6 space-x-3">
                                    <img className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="Tech"/>
                                <div className="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
                                        <div className="pr-3 font-medium text-gray-900 dark:text-white">TechCorp</div>
                                    </div>
                                </figcaption>
                            </figure>
                        </div>
                    </section>
                    <section className="bg-white dark:bg-gray-900">
                        <div className="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-16 lg:px-6">
                            <figure className="max-w-screen-md mx-auto">
                                <svg className="h-12 mx-auto mb-3 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor"/>
                                </svg> 
                                <blockquote>
                                    <p className="text-2xl font-medium text-gray-900 dark:text-white">"The internship tracking feature helped me stay on top of my progress and ensured I met all my goals. Highly recommend S&C!"</p>
                                </blockquote>
                                <figcaption className="flex items-center justify-center mt-6 space-x-3">
                                <img className="w-6 h-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/bonnie-green.png" alt="profile"/>
                                    <div className="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
                                        <div className="pr-3 font-medium text-gray-900 dark:text-white">Alice</div>
                                    </div>
                                </figcaption>
                            </figure>
                        </div>
                    </section>
                </div>
            </div>
            <Footer />
        </div>
        
    );
};

export default About;
