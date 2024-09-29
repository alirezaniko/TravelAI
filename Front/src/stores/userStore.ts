import { defineStore } from 'pinia';

interface User {
  pk: number;
  email: string;
  // Add other user properties as needed
}

export const useUserStore = defineStore('user', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('user') || 'null') as User | null, // Load user from local storage
  }),
  actions: {
    setUser(userData: User) {
      this.user = userData; // Set the user data
      localStorage.setItem('user', JSON.stringify(userData)); // Persist to local storage
    },
    clearUser() {
      this.user = null; // Clear the user data
      localStorage.removeItem('user'); // Remove from local storage
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.user, // Return true if user is set
  },
});
