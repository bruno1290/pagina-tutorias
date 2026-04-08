const supabaseUrl = 'https://ikwnjgqfaetypszhldxl.supabase.co';
const supabaseKey = 'sb_publishable_Ds-YxDoEWk4PeWz7yN2A8Q_2hmgyuWG';

// Inicializar el cliente de Supabase
const supabaseClient = window.supabase.createClient(supabaseUrl, supabaseKey);

// Objeto global de Auth para ayudar a toda la página
const AppAuth = {
    // Función para revisar si hay una sesión activa y redirigir si es necesario
    async checkSession(requireAuth = false, redirectIfLoggedIn = false) {
        const { data: { session } } = await supabaseClient.auth.getSession();
        
        if (requireAuth && !session) {
            window.location.href = 'login.html';
            return null;
        }

        if (redirectIfLoggedIn && session) {
            // Verificar rol para redirigir al portal correcto
            const { data: profile } = await supabaseClient
                .from('perfiles')
                .select('rol')
                .eq('id', session.user.id)
                .single();
                
            if (profile && profile.rol === 'admin') {
                window.location.href = 'portal-admin.html';
            } else {
                window.location.href = 'portal-tutor.html';
            }
            return session;
        }
        
        return session;
    },

    async logout() {
        await supabaseClient.auth.signOut();
        window.location.href = 'index.html';
    }
};
