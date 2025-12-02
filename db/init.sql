CREATE TABLE IF NOT EXISTS tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  completed BOOLEAN NOT NULL DEFAULT false
);

INSERT INTO tasks (title, completed) VALUES
('Comprar leche', false),
('Estudiar para la entrega final', false),
('Enviar informe', true)
ON CONFLICT DO NOTHING;

