-- ==============================================================================
-- EJECUTA ESTO EN EL SQL EDITOR DE SUPABASE
-- Este script crea las tablas necesarias para la página de tutorías.
-- Si recibes errores de que algo "ya existe", es porque ya se creó parcialmente.
-- ==============================================================================

-- 1. Crear tabla de perfiles (Tutores y Administradores)
CREATE TABLE IF NOT EXISTS public.perfiles (
  id uuid REFERENCES auth.users ON DELETE CASCADE NOT NULL PRIMARY KEY,
  nombre_completo text,
  rol text DEFAULT 'tutor',
  nombre_atutorado text
);

-- Asegurar nivel de seguridad
ALTER TABLE public.perfiles ENABLE ROW LEVEL SECURITY;

-- Borrar políticas si existen para evitar errores al re-ejecutar
DROP POLICY IF EXISTS "Cualquier usuario autenticado puede leer los perfiles" ON perfiles;
DROP POLICY IF EXISTS "Los usuarios pueden insertar su propio perfil al registrarse" ON perfiles;

-- Políticas de seguridad
CREATE POLICY "Cualquier usuario autenticado puede leer los perfiles"
  ON perfiles FOR SELECT
  USING ( auth.role() = 'authenticated' );

CREATE POLICY "Los usuarios pueden insertar su propio perfil al registrarse"
  ON perfiles FOR INSERT
  WITH CHECK ( auth.uid() = id );


-- 2. Crear tabla de Registro de Clases / Asistencia
CREATE TABLE IF NOT EXISTS public.sesiones_clases (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  tutor_id uuid REFERENCES public.perfiles(id) NOT NULL,
  fecha date NOT NULL DEFAULT CURRENT_DATE,
  asistencia text NOT NULL,
  notas_desempeno text
);

-- Asegurar nivel de seguridad
ALTER TABLE public.sesiones_clases ENABLE ROW LEVEL SECURITY;

-- Borrar políticas si existen
DROP POLICY IF EXISTS "Usuarios autenticados pueden leer las sesiones" ON sesiones_clases;
DROP POLICY IF EXISTS "Los tutores pueden insertar las sesiones de su propia cuenta" ON sesiones_clases;

-- Políticas de seguridad para las sesiones
CREATE POLICY "Usuarios autenticados pueden leer las sesiones"
  ON sesiones_clases FOR SELECT
  USING ( auth.role() = 'authenticated' );

CREATE POLICY "Los tutores pueden insertar las sesiones de su propia cuenta"
  ON sesiones_clases FOR INSERT
  WITH CHECK ( auth.uid() = tutor_id );
