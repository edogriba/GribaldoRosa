import React from "react"

const StudentList = () => {
    return (
        <div>    
            <section class="bg-white py-8 antialiased dark:bg-gray-900 md:py-16">
                <div class="mx-auto max-w-screen-xl px-4 2xl:px-0">
                    <div class="mx-auto max-w-5xl">
                    <div class="gap-4 lg:flex lg:items-center lg:justify-between">
                        <h2 class="text-xl font-semibold text-gray-900 dark:text-white sm:text-2xl">My applications</h2>

                        <div class="mt-6 gap-4 space-y-4 sm:flex sm:items-center sm:space-y-0 lg:mt-0 lg:justify-end">
                        <div>
                            <label for="order-type" class="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white">Select order type</label>
                            <select id="order-type" class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]">
                            <option selected>All applications</option>
                            <option value="ongoing">Ongoing</option>
                            <option value="completed">Completed</option>
                            <option value="denied">Denied</option>
                            </select>
                        </div>

                        <span class="inline-block text-gray-500 dark:text-gray-400"> from </span>

                        <div>
                            <label for="date" class="sr-only mb-2 block text-sm font-medium text-gray-900 dark:text-white">Select date</label>
                            <select id="date" class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500 sm:w-[144px]">
                            <option selected>this week</option>
                            <option value="this month">this month</option>
                            <option value="last 3 months">the last 3 months</option>
                            <option value="lats 6 months">the last 6 months</option>
                            <option value="this year">this year</option>
                            </select>
                        </div>

                        <button type="button" class="w-full rounded-lg bg-primary-700 px-5 py-2.5 text-sm font-medium text-white hover:bg-primary-800 focus:outline-none focus:ring-4 focus:ring-primary-300   dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 sm:w-auto">Add return request</button>
                        </div>
                    </div>

                    <div class="mt-6 flow-root sm:mt-8">
                        <div class="divide-y divide-gray-200 dark:divide-gray-700">
                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB127364372</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">22 May 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Missing parts</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class="inline-flex items-center rounded bg-primary-100 px-2.5 py-0.5 text-xs font-medium text-primary-800 dark:bg-primary-900 dark:text-primary-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.5 4h-13m13 16h-13M8 20v-3.333a2 2 0 0 1 .4-1.2L10 12.6a1 1 0 0 0 0-1.2L8.4 8.533a2 2 0 0 1-.4-1.2V4h8v3.333a2 2 0 0 1-.4 1.2L13.957 11.4a1 1 0 0 0 0 1.2l1.643 2.867a2 2 0 0 1 .4 1.2V20H8Z" />
                                </svg>
                                Ongoing
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>

                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB746253940</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">06 April 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Wrong item</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class="  inline-flex items-center rounded bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 dark:bg-green-900 dark:text-green-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                </svg>
                                Completed
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>

                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB453648693</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">24 March 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Defective item</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class=" inline-flex items-center rounded bg-red-100 px-2.5 py-0.5 text-xs font-medium text-red-800 dark:bg-red-900 dark:text-red-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18 17.94 6M18 18 6.06 6" />
                                </svg>
                                Denied
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>

                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB234826346</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">24 February 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Color mismatch</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class="  inline-flex items-center rounded bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 dark:bg-green-900 dark:text-green-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                </svg>
                                Completed
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>
                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB127364372</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">12 April 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Missing parts</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class="inline-flex items-center rounded bg-primary-100 px-2.5 py-0.5 text-xs font-medium text-primary-800 dark:bg-primary-900 dark:text-primary-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.5 4h-13m13 16h-13M8 20v-3.333a2 2 0 0 1 .4-1.2L10 12.6a1 1 0 0 0 0-1.2L8.4 8.533a2 2 0 0 1-.4-1.2V4h8v3.333a2 2 0 0 1-.4 1.2L13.957 11.4a1 1 0 0 0 0 1.2l1.643 2.867a2 2 0 0 1 .4 1.2V20H8Z" />
                                </svg>
                                Ongoing
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>

                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB746253940</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">30 April 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Wrong item</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class="  inline-flex items-center rounded bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 dark:bg-green-900 dark:text-green-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                </svg>
                                Completed
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>

                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB453648693</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">12 May 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Defective item</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class=" inline-flex items-center rounded bg-red-100 px-2.5 py-0.5 text-xs font-medium text-red-800 dark:bg-red-900 dark:text-red-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18 17.94 6M18 18 6.06 6" />
                                </svg>
                                Denied
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>

                        <div class="relative grid grid-cols-2 gap-4 py-6 sm:grid-cols-4 lg:grid-cols-5">
                            <div class="col-span-2 content-center sm:col-span-4 lg:col-span-1">
                            <a href="#" class="text-base font-semibold text-gray-900 hover:underline dark:text-white">#FWB234826346</a>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center gap-2">
                                <svg class="h-4 w-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z" />
                                </svg>
                                <p class="text-sm font-medium text-gray-500 dark:text-gray-400">23 June 2024</p>
                            </div>
                            </div>

                            <div class="content-center">
                            <div class="flex items-center justify-end gap-2 sm:justify-start">
                                <p class="text-sm text-gray-500 dark:text-gray-400"><span class="font-medium text-gray-900 dark:text-white">Reason</span>: Color mismatch</p>
                            </div>
                            </div>

                            <div class="absolute right-0 top-7 content-center sm:relative sm:right-auto sm:top-auto">
                            <span class="  inline-flex items-center rounded bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 dark:bg-green-900 dark:text-green-300">
                                <svg class="me-1 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 11.917 9.724 16.5 19 7.5" />
                                </svg>
                                Completed
                            </span>
                            </div>

                            <div class="col-span-2 content-center sm:col-span-1 sm:justify-self-end">
                            <button type="button" class="w-full rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700 sm:w-auto">View details</button>
                            </div>
                        </div>
                        </div>
                    </div>

                    <nav class="mt-2 flex items-center justify-center sm:mt-8" aria-label="Page navigation example">
                        <ul class="flex h-8 items-center -space-x-px text-sm">
                        <li>
                            <a href="#" class="ms-0 flex h-8 items-center justify-center rounded-s-lg border border-e-0 border-gray-300 bg-white px-3 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                            <span class="sr-only">Previous</span>
                            <svg class="h-4 w-4 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m15 19-7-7 7-7" />
                            </svg>
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex h-8 items-center justify-center border border-gray-300 bg-white px-3 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
                        </li>
                        <li>
                            <a href="#" class="flex h-8 items-center justify-center border border-gray-300 bg-white px-3 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
                        </li>
                        <li>
                            <a href="#" aria-current="page" class="z-10 flex h-8 items-center justify-center border border-primary-300 bg-primary-50 px-3 leading-tight text-primary-600 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
                        </li>
                        <li>
                            <a href="#" class="flex h-8 items-center justify-center border border-gray-300 bg-white px-3 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">...</a>
                        </li>
                        <li>
                            <a href="#" class="flex h-8 items-center justify-center border border-gray-300 bg-white px-3 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">100</a>
                        </li>
                        <li>
                            <a href="#" class="flex h-8 items-center justify-center rounded-e-lg border border-gray-300 bg-white px-3 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                            <span class="sr-only">Next</span>
                            <svg class="h-4 w-4 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m9 5 7 7-7 7" />
                            </svg>
                            </a>
                        </li>
                        </ul>
                    </nav>
                    </div>
                </div>
            </section>
        </div>
    )
}

export default StudentList;