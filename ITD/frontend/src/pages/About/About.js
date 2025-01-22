import React from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';

const About = () => {
    return (
        <div>
            <Navbar currentPage="about"/>
        <div className="container mx-auto p-4">
            <div class="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">S&C (Students & Companies)</h2>
                <p class="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">                S&C is a startup founded at Politecnico di Milano that offers an innovative web application for students to look for internships and for companies to offer internships. It helps track the progress of undertaken internships and lets universities monitor their students' internship progress as well.</p>
            </div> 

            <div class="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Story</h2>
                <p class="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">It all began with a Software Engineering 2 assignment!</p>
            </div> 
            <ol className="relative border-l border-gray-200 dark:border-gray-700">
                <li className="mb-10 ms-4">
                    <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                    <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">October 2024</time>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Foundation</h3>
                    <p className="text-base font-normal text-gray-500 dark:text-gray-400">
                        Edoardo and Federico, two students from Politecnico di Milano, founded S&C with the vision to bridge the gap between students and companies.
                    </p>
                </li>
                <li className="mb-10 ms-4">
                    <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                    <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">Febraury 2025</time>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Launch</h3>
                    <p className="text-base font-normal text-gray-500 dark:text-gray-400">
                        The S&C platform was launched, providing a seamless experience for students to find internships and for companies to offer them.
                    </p>
                </li>
                <li className="mb-10 ms-4">
                    <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                    <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">March 2025 - Now</time>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Growth</h3>
                    <p className="text-base font-normal text-gray-500 dark:text-gray-400">
                        S&C expanded its services, allowing universities to monitor their students' internship progress, ensuring a comprehensive internship experience.
                    </p>
                </li>
            </ol>
            <h2 className="text-3xl font-semibold mb-4">Our Founders</h2>
            <section class="bg-white dark:bg-gray-900">
                <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6 ">
                    <div class="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                        <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Team</h2>
                        <p class="font-light text-gray-500 lg:mb-16 sm:text-xl dark:text-gray-400">Explore the whole collection of open-source web components and elements built with the utility classes from Tailwind</p>
                    </div> 
                    <div class="grid gap-8 mb-6 lg:mb-16 md:grid-cols-2">
                        <div class="items-center bg-gray-50 rounded-lg shadow sm:flex dark:bg-gray-800 dark:border-gray-700">
                            <a href="#">
                                <img class="w-full rounded-lg sm:rounded-none sm:rounded-l-lg" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="Bonnie Avatar"/>
                            </a>
                            <div class="p-5">
                                <h3 class="text-xl font-bold tracking-tight text-gray-900 dark:text-white">
                                    <a href="#">Edoardo Gribaldo</a>
                                </h3>
                                <span class="text-gray-500 dark:text-gray-400">Co-Founder</span>
                                <p class="mt-3 mb-4 font-light text-gray-500 dark:text-gray-400">Edoardo is passionate about computer science and creating this startup was a dream come true for him.</p>
                                <ul class="flex space-x-4 sm:mt-0">
                                    <li>
                                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path fill-rule="evenodd" d="M12.51 8.796v1.697a3.738 3.738 0 0 1 3.288-1.684c3.455 0 4.202 2.16 4.202 4.97V19.5h-3.2v-5.072c0-1.21-.244-2.766-2.128-2.766-1.827 0-2.139 1.317-2.139 2.676V19.5h-3.19V8.796h3.168ZM7.2 6.106a1.61 1.61 0 0 1-.988 1.483 1.595 1.595 0 0 1-1.743-.348A1.607 1.607 0 0 1 5.6 4.5a1.601 1.601 0 0 1 1.6 1.606Z" clip-rule="evenodd" />
                                            <path d="M7.2 8.809H4V19.5h3.2V8.809Z" />
                                            </svg>  
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div> 
                        <div class="items-center bg-gray-50 rounded-lg shadow sm:flex dark:bg-gray-800 dark:border-gray-700">
                            <a href="#">
                                <img class="w-full rounded-lg sm:rounded-none sm:rounded-l-lg" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/jese-leos.png" alt="Jese Avatar" />
                            </a>
                            <div class="p-5">
                                <h3 class="text-xl font-bold tracking-tight text-gray-900 dark:text-white">
                                    <a href="#">Federico Rosa</a>
                                </h3>
                                <span class="text-gray-500 dark:text-gray-400">Co-Founder</span>
                                <p class="mt-3 mb-4 font-light text-gray-500 dark:text-gray-400">Federico loves Computer Science and this startup was a great chance to put to work his ideas.</p>
                                <ul class="flex space-x-4 sm:mt-0">
                                    <li>
                                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" /></svg>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path fill-rule="evenodd" d="M12.51 8.796v1.697a3.738 3.738 0 0 1 3.288-1.684c3.455 0 4.202 2.16 4.202 4.97V19.5h-3.2v-5.072c0-1.21-.244-2.766-2.128-2.766-1.827 0-2.139 1.317-2.139 2.676V19.5h-3.19V8.796h3.168ZM7.2 6.106a1.61 1.61 0 0 1-.988 1.483 1.595 1.595 0 0 1-1.743-.348A1.607 1.607 0 0 1 5.6 4.5a1.601 1.601 0 0 1 1.6 1.606Z" clip-rule="evenodd" />
                                            <path d="M7.2 8.809H4V19.5h3.2V8.809Z" />
                                            </svg>  
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div> 
                    </div>  
                </div>
            </section>
            <div class="mx-auto max-w-screen-sm text-center mb-8 lg:mb-16">
                <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white">Our Success Stories</h2>
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
                                <img className="w-6 h-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile"/>
                                <div className="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
                                    <div className="pr-3 font-medium text-gray-900 dark:text-white">Alice</div>
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
                                <img className="w-6 h-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile"/>
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
                                <img className="w-6 h-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile"/>
                                <div className="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
                                    <div className="pr-3 font-medium text-gray-900 dark:text-white">Marco</div>
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
